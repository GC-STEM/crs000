# Course Development Environments

This folder configures the course's **Standard Operating Environment (SOE)**
plus any **Course-Specific Overlay (CSO)** requirements defined in
[`.config/cso_manifest.json`](../.config/cso_manifest.json).

The canonical SOE manifest and provisioning scripts are maintained in
[GC-STEM/SOE](https://github.com/GC-STEM/SOE), and the JSON schema is maintained
in [GC-STEM/.github](https://github.com/GC-STEM/.github/tree/main/schemas).
The current target is **Ubuntu 24.04 LTS, CPython 3.12, AMD64**. Codio remains
the reference course environment when provided.

## GitHub Codespaces

Open the course repository on GitHub and select **Code > Codespaces > Create
codespace**. Its `devcontainer.json` builds the image using a pinned SOE source
snapshot. On creation, the SOE automation applies the course CSO. Subsequent
startups verify the runtime, and editor attachment checks VS Code extensions.

The Dockerfile's `SOE_COMMIT` argument selects the tested SOE revision. Update
that reference deliberately when qualifying an SOE update, then rebuild the
container. Codespaces availability, limits, and billing depend on the user's
GitHub account and organization settings.

## Local Docker

Install Docker with the Compose plugin. From the **course repository root**,
run:

```bash
docker compose -f .devcontainer/compose.local.yaml run --build --rm soe
```

This builds the same Ubuntu image, mounts the course checkout at
`/workspaces/course`, applies its CSO, then opens a Bash shell. Local changes
are written to the course checkout on the host. A new interactive session
runs setup again, which should be safe to repeat, but may perform package
installation when requirements are missing. The SOE script is bundled into
the image at `/opt/gc-stem/soe/scripts/python/soe.py`.

To verify the course from inside the container, run:

```bash
/opt/gc-stem/runtime/bin/python /opt/gc-stem/soe/scripts/python/soe.py verify --workspace /workspaces/course
```

The local Docker option does not include a Linux desktop, and its startup
does not automatically install the editor extensions available in Codespaces.

## Windows Sandbox

`Sandboxfile.wsb` launches a disposable Windows test environment and downloads
[the SOE Windows Sandbox bootstrap](https://github.com/GC-STEM/SOE/blob/main/scripts/pwsh/setup_windows_sandbox.ps1).
The bootstrap reads the SOE and CSO manifests and installs supported Windows
tools. It is designed for faculty/testing, not persistent student course work.
Changes inside Windows Sandbox are lost when it closes. The bootstrap must be
qualified on a clean Sandbox installation before claiming it is ready for use.

## Vagrant

`Vagrantfile` is an **intentional placeholder**. It does not configure a
working VM, and `vagrant up` is not a supported course setup path yet.

## Maintenance

Keep SOE packages and automation in `GC-STEM/SOE`; do not copy them into each
course. Course-specific requirements belong in `.config/cso_manifest.json`.
Rebuild Codespaces or Docker images after changing the selected SOE revision.
