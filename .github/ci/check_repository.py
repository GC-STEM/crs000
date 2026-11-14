"""Validate shared configuration using a repository requirements manifest."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tomllib
from pathlib import Path
from typing import TypedDict, cast

import editorconfig
import json5
import yaml

ROOT = Path(__file__).resolve().parents[2]


class RepositoryPolicy(TypedDict):
    """Required configuration for repository validation."""

    required_files: list[str]
    ide_samples: dict[str, str]


def string_mapping(value: object) -> dict[str, object] | None:
    """Return a mapping with string keys, or None if invalid."""
    if not isinstance(value, dict):
        return None

    mapping = cast(dict[object, object], value)
    if not all(isinstance(key, str) for key in mapping):
        return None

    return cast(dict[str, object], mapping)


def load_policy(value: object) -> RepositoryPolicy:
    """Validate an untrusted repository policy document."""
    data = string_mapping(value)
    if data is None:
        raise ValueError("Repository policy must be a JSON object.")

    files = data.get("required_files")
    if not isinstance(files, list):
        raise ValueError("Policy required_files must be a list.")

    candidates = cast(list[object], files)
    required_files = [
        item for item in candidates if isinstance(item, str)
    ]
    if len(required_files) != len(candidates):
        raise ValueError("Policy required_files must contain strings.")

    samples = string_mapping(data.get("ide_samples"))
    if samples is None:
        raise ValueError("Policy ide_samples must be an object.")

    ide_samples = {
        key: item
        for key, item in samples.items()
        if isinstance(item, str)
    }
    if len(ide_samples) != len(samples):
        raise ValueError("Policy ide_samples values must be strings.")

    return {
        "required_files": required_files,
        "ide_samples": ide_samples,
    }


def tracked_files(root: Path) -> list[Path]:
    """Include hidden files without scanning virtual environments or .git."""
    result = subprocess.run(
        ["git", "ls-files", "-z"], cwd=root, check=True, capture_output=True
    )
    return [
        root / name
        for name in result.stdout.decode("utf-8").split("\0")
        if name
    ]


def git_eol(root: Path, names: list[str]) -> dict[str, str]:
    """Ask Git to resolve attributes, including ordered filename exceptions."""
    result = subprocess.run(
        ["git", "check-attr", "-z", "--stdin", "eol"],
        input="\0".join(names).encode(),
        cwd=root,
        capture_output=True,
        check=True,
    )
    fields = result.stdout.decode().split("\0")
    return dict(zip(fields[0::3], fields[2::3]))


def eol_samples(root: Path) -> list[str]:
    """Cover each explicit EoL rule and the current tracked text files."""
    names: set[str] = set()

    for line in (root / ".gitattributes").read_text().splitlines():
        parts = line.split()
        if not parts or parts[0].startswith("#"):
            continue
        if any(part.startswith("eol=") for part in parts[1:]):
            pattern = parts[0]
            if re.search(r"[?\[\]]", pattern):
                raise ValueError(
                    f"Add representative samples for complex pattern: {pattern}"
                )
            # Current baseline uses extension patterns and exact filenames.
            names.add(pattern.replace("*", "example"))
            names.add("nested/" + pattern.replace("*", "example"))

    names.update(
        path.relative_to(root).as_posix() for path in tracked_files(root)
    )
    return sorted(names)


def editor_eol(path: Path) -> str | None:
    """Return the resolved EditorConfig line ending, when defined."""
    properties = cast(
        dict[str, object],
        editorconfig.get_properties(str(path)),
    )
    value = properties.get("end_of_line")
    return value if isinstance(value, str) else None


def check_eol(
    root: Path,
    policy: RepositoryPolicy,
    settings: dict[str, object],
) -> tuple[list[str], list[str]]:
    """Check policy agreement, not working-tree bytes normalized by Git."""
    errors: list[str] = []
    warnings: list[str] = []

    samples = eol_samples(root)
    attributes = git_eol(root, samples)

    for name in samples:
        expected = attributes[name]
        actual = editor_eol(root / name)

        if expected in {"lf", "crlf"} and actual != expected:
            errors.append(
                f"EoL policy mismatch: {name}: Git={expected}, "
                f"EditorConfig={actual or 'unset'}."
            )

    missing: list[str] = []

    for language, name in policy["ide_samples"].items():
        expected = editor_eol(root / name)

        # VS Code supports single and compound language override keys.
        values: set[str] = set()

        for key, value in settings.items():
            if f"[{language}]" not in key:
                continue

            override = string_mapping(value)
            if override is None:
                continue

            file_eol = override.get("files.eol")
            if isinstance(file_eol, str):
                values.add(file_eol)

        if not values:
            default_eol = settings.get("files.eol", "auto")
            values = (
                {default_eol}
                if isinstance(default_eol, str)
                else {"auto"}
            )

        desired = (
            {"lf": "\n", "crlf": "\r\n"}.get(expected)
            if expected is not None
            else None
        )
        if desired is None:
            continue

        if "auto" in values:
            missing.append(language)

        for value in values - {"auto"}:
            if value != desired:
                errors.append(
                    f"VS Code EoL conflicts with EditorConfig: {language}."
                )

    if missing:
        warnings.append(
            "VS Code files.eol safeguard is unset/auto for: "
            + ", ".join(missing)
            + ". Review .vscode/settings.json separately."
        )

    return errors, warnings


def check_workflow(name: str, data: object) -> list[str]:
    """Validate required GitHub Actions workflow safeguards."""
    errors: list[str] = []
    workflow = string_mapping(data)

    if workflow is None:
        return [f"Empty/invalid workflow: {name}"]

    for key in ("name", "on", "jobs", "permissions"):
        if not workflow.get(key):
            errors.append(f"{name}: missing {key}.")

    if workflow.get("permissions") != {"contents": "read"}:
        errors.append(f"{name}: use contents: read only.")

    triggers = workflow.get("on")
    trigger_mapping = string_mapping(triggers)

    if triggers == "pull_request_target" or (
        trigger_mapping is not None
        and "pull_request_target" in trigger_mapping
    ):
        errors.append(f"{name}: privileged PR event disallowed.")

    jobs = string_mapping(workflow.get("jobs"))
    if jobs is None:
        errors.append(f"{name}: jobs must be a mapping.")
        return errors

    for job_name, job_value in jobs.items():
        job = string_mapping(job_value)
        if job is None:
            errors.append(f"{name}: invalid job: {job_name}.")
            continue

        steps_value = job.get("steps", [])
        if not isinstance(steps_value, list):
            errors.append(f"{name}: invalid steps in {job_name}.")
            continue

        steps = cast(list[object], steps_value)

        for step_value in steps:
            step = string_mapping(step_value)
            if step is None:
                errors.append(f"{name}: invalid step in {job_name}.")
                continue

            uses = step.get("uses", "")
            if not isinstance(uses, str):
                errors.append(f"{name}: invalid action in {job_name}.")
            elif uses and not uses.startswith("./"):
                if not re.search(r"@[a-f0-9]{40}$", uses):
                    errors.append(
                        f"{name}: pin action to full SHA: {uses}"
                    )

            options = string_mapping(step.get("with"))
            if options is not None:
                if options.get("persist-credentials") == "true":
                    errors.append(
                        f"{name}: credentials must not persist."
                    )

    return errors


def validate(
    root: Path,
    policy: RepositoryPolicy,
) -> tuple[list[str], list[str]]:
    """Parse repository configuration and validate reusable Core safeguards."""
    errors: list[str] = []
    warnings: list[str] = []

    paths = tracked_files(root)

    # Faculty-only content must never be tracked in a student repository.
    for path in paths:
        relative = path.relative_to(root)
        if any(
            part.casefold() == ".faculty"
            for part in relative.parts[:-1]
        ):
            errors.append(
                f"Faculty-only directory is tracked: {relative.as_posix()}"
            )

    for name in policy["required_files"]:
        path = root / name
        if not path.is_file() or not path.stat().st_size:
            errors.append(f"Required file is missing or empty: {name}")

    settings: dict[str, object] = {}

    for path in paths:
        if not path.is_file():
            continue

        name = path.relative_to(root).as_posix()

        try:
            source = path.read_text(encoding="utf-8")

            if path.suffix in {".json", ".jsonc", ".code-workspace"}:
                # VS Code accepts comments and trailing commas.
                if name.startswith(".vscode/") or path.suffix != ".json":
                    data: object = json5.loads(
                        source, allow_duplicate_keys=False
                    )
                else:
                    data = json.loads(source)

                if name == ".vscode/settings.json":
                    parsed_settings = string_mapping(data)
                    if parsed_settings is None:
                        raise ValueError(
                            "VS Code settings must be a JSON object."
                        )
                    settings = parsed_settings

            elif path.suffix == ".toml":
                tomllib.loads(source)

            elif path.suffix in {".yml", ".yaml"}:
                # BaseLoader keeps Actions' 'on' from becoming YAML 1.1 True.
                data = yaml.load(source, Loader=yaml.BaseLoader)

                if name.startswith(".github/workflows/"):
                    errors.extend(check_workflow(name, data))
                elif data is None:
                    warnings.append(
                        f"Empty configuration awaits review: {name}"
                    )

        except UnicodeDecodeError:
            # Binary assets are not text configuration.
            continue
        except (ValueError, yaml.YAMLError) as error:
            errors.append(f"{name}: invalid configuration: {error}")

    try:
        eol_errors, eol_warnings = check_eol(root, policy, settings)
        errors.extend(eol_errors)
        warnings.extend(eol_warnings)
    except (OSError, ValueError, editorconfig.EditorConfigError) as error:
        errors.append(f"Cannot validate EoL policy: {error}")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument(
        "--policy", type=Path, default=ROOT / ".github/ci/core-policy.json"
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat existing review warnings as failures.",
    )

    args = parser.parse_args()
    root = cast(Path, args.root)
    policy_path = cast(Path, args.policy)
    strict = cast(bool, args.strict)

    try:
        policy_data: object = json.loads(
            policy_path.read_text(encoding="utf-8")
        )
        policy = load_policy(policy_data)
    except (OSError, ValueError) as error:
        print(f"ERROR: Invalid repository policy: {error}", file=sys.stderr)
        return 1

    errors, warnings = validate(root.resolve(), policy)

    for warning in warnings:
        print(f"WARNING: {warning}")

    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)

    print(
        f"Repository validation: {len(errors)} error(s), "
        f"{len(warnings)} warning(s)."
    )

    return int(bool(errors or (strict and warnings)))


if __name__ == "__main__":
    raise SystemExit(main())
