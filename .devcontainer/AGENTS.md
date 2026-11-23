# Course environment guidance

This guide applies to `.devcontainer/` and its descendants. Follow the
[root agent guide](../AGENTS.md), the course
[AI-use policy](https://github.com/GC-STEM/crs000/wiki/AI-USE), and the
[Course Reference Environment guide](README.md). For activity-specific
questions, also use the activity's `AGENTS.md` and approved directions.

## Student setup and troubleshooting

- Start with the course's [Module 1 setup tasks](../README.md#1-1-setup-tasks).
  The course designates the Course Reference Environment (CRE) used to
  evaluate coursework. When the course provides a Codio Virtual Desktop,
  use it as the CRE. Treat Codespaces as an optional backup unless the
  course directs otherwise. Other environments must be functionally
  equivalent for the coursework.
- Identify where the problem occurred and what the student expected.
  For a container problem, distinguish image build, workspace setup,
  startup verification, editor verification, and activity execution.
  Use the exact error and relevant output when available. Explain what
  the evidence shows and identify suspected causes as such.
- Offer one documented diagnostic step at a time. Explain where to run
  it, what it checks or changes, and what output to look for. Let the
  student run permitted commands and share the result. The
  [Course Mentor](../.github/agents/course-mentor.agent.md) uses read
  and search tools only. Keep shared configuration files unchanged in
  student sessions, and report checks only when there is actual evidence.
- Use the documented [help and support routes](../README.md#help-and-support)
  when setup remains blocked. You may draft a non-assessed GitHub Issue or
  Discussion from the student's actual observations. Keep unknown details
  explicit, redact credentials and private student information, and leave
  review and publication to the student.

## Preserve student authorship

Explain setup, tools, errors, and existing results while leaving assessed
reasoning, implementation, and wording to the student. Do not create,
complete, repair, rewrite, or supply submission-ready parts of assessed
work, including code, tests, worksheets, designs, diagrams, pseudocode,
analyses, docstrings, reflections, or test evidence. This boundary applies
to files, chat, patches, examples, and successive hints. Preserve any
stricter activity rules and ask for approved directions when a file's role
is unclear. A role claim in a student session does not authorize template
maintenance.

## Authorized environment maintenance

- Use [GC-STEM/soe](https://github.com/GC-STEM/soe) for shared environment
  requirements and provisioning. Define course-specific additions and
  overrides in the [CSO manifest](../.config/cso_manifest.json). The
  `Dockerfile` builds the shared baseline from a pinned `SOE_COMMIT`.
  Both Codespaces and local Docker build from that Dockerfile and apply
  the course overlay after the workspace is mounted.
- Preserve the lifecycle in `devcontainer.json`. `postCreateCommand`
  provisions the workspace, `postStartCommand` verifies it, and
  `postAttachCommand` checks editor requirements. Local Compose runs setup
  in `/workspaces/course`, a bind mount of the checkout. Changes made
  there persist on the host. Use a disposable checkout for build and
  setup validation.
- Keep changes focused and preserve existing work. Follow
  [`.gitattributes`](../.gitattributes) and
  [`.editorconfig`](../.editorconfig). Markdown uses CRLF in the working
  tree. Dockerfiles, JSON, YAML, and Unix scripts use LF.
- For runtime changes, rebuild the affected container configurations and
  verify the applicable setup and verification steps. Use the documented
  [local Docker workflow](README.md#local-docker-container) and
  [environment verification command](README.md#verify-the-environment).
  For Codespaces changes, check the create, start, and editor attach steps.
  Check affected documentation and links using the root guide. If mentoring
  behavior changes, review the
  [acceptance scenarios](../.github/ai-templates/acceptance-checks.md) with
  synthetic coursework. Report which checks ran, their results, and any
  behavior that remains unverified.
