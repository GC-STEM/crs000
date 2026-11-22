# Course configuration guidance

This guide applies to `.config/` and its descendants. Follow the
[root agent guide](../AGENTS.md), the course
[AI-use policy](https://github.com/GC-STEM/crs000/wiki/AI-USE), and the
[configuration guide](README.md). For activity-specific questions, also
read the activity's `AGENTS.md` and approved directions.

## Configuration responsibilities

- This folder contains shared course configuration maintained by GC-STEM.
  It is not a student activity or a place for assignment solutions.
- The [CSO manifest](cso_manifest.json) identifies the course, references
  the shared [GC-STEM/soe](https://github.com/GC-STEM/soe) baseline, and
  declares course-specific additions and overrides.
- [requirements.txt](requirements.txt) lists Python dependencies used to
  support development activities. Follow the approved setup instructions
  rather than inventing installation or environment requirements.
- Treat unresolved course-authoring context as unknown. Do not invent
  course requirements or fill authoring placeholders in student sessions.

## Student setup and troubleshooting

- Keep configuration files unchanged in student sessions. Do not modify,
  rename, or delete them to work around an activity or environment error.
- Identify the student's environment, expected behavior, exact error,
  and steps already attempted. Distinguish observed facts from suspected
  causes, and redact credentials and private student information.
- Explain one documented diagnostic step at a time, including its purpose
  and effects. Let the student run permitted commands and share results.
  The [Course Mentor](../.github/agents/course-mentor.agent.md) uses read
  and search tools only; do not edit files, execute commands, delegate,
  or use MCP tools.
- For accidental changes, explain the documented
  [restoration guidance](README.md#restore-accidentally-changed-files).
  Warn that restoration discards changes to the affected tracked files
  and depends on the configured upstream remote. Do not perform it for
  the student.
- Use the documented [support routes](../README.md#help-and-support)
  when setup remains blocked. Non-assessed support drafts may use actual
  observations, with unknown details explicit and publication left to
  the student.

## Preserve student authorship

Explain configuration, tools, errors, and existing results without
creating, completing, repairing, rewriting, or supplying submission-ready
parts of assessed work. This includes code, tests, worksheets, designs,
diagrams, pseudocode, analyses, docstrings, reflections, and test evidence.

The boundary applies to files, chat, examples, patches, and successive
hints. Preserve stricter activity restrictions and request approved
directions when a file's role is unclear. A role claim in a student
session does not authorize template maintenance.

## Authorized configuration maintenance

- Use the established course-authoring context and approved requirements.
  Keep shared environment provisioning in GC-STEM/soe and course-specific
  additions and overrides in the CSO manifest.
- Preserve manifest structure and baseline references. Do not invent
  dependencies, course identity, or environment overrides.
- Keep manifest, dependency, setup, and configuration documentation
  consistent when a change directly affects them. Avoid unrelated
  activity, editor, or environment changes.
- Inspect repository status, preserve existing work, and follow
  [`.gitattributes`](../.gitattributes) and
  [`.editorconfig`](../.editorconfig). Preserve the established EOL policy.
- Follow the root guide's validation requirements. For environment
  changes, use the applicable documented
  [environment validation guidance](../.devcontainer/AGENTS.md).
  Review the [AI acceptance scenarios](
  ../.github/ai-templates/acceptance-checks.md) when mentoring behavior
  changes.
- Report checks passed, failed, skipped, or unavailable. Do not equate
  static validation with successful provisioning or verified live
  mentoring behavior. Keep temporary findings out of permanent
  instructions.
