# Authoring the course AI package

This directory contains source-template material for course authors. The
student mentoring policy is in [AI-USE.md](https://github.com/GC-STEM/crs000/wiki/AI-USE). Keep authoring
sources upstream; prepare a configured release before distributing a course
repository to students.

## File responsibilities

| File or directory | Responsibility |
| --- | --- |
| Root `AI-USE.md` | Student explanation of useful help, authorship, privacy, and support. |
| Root `AGENTS.md` | Agent workflow, essential boundary, repository context, and authorized maintenance. |
| `.github/copilot-instructions.md` | Concise, self-contained Copilot mentoring guidance. |
| `.github/instructions/student-mentoring.instructions.md` | Shared activity guidance scoped to the current activity folders. |
| Each activity's `AGENTS.md` | Verified local context, protected deliverables, references, and appropriate help. |
| `.github/agents/course-mentor.agent.md` | Selectable Course Mentor with read/search tools. |
| `.github/skills/*/SKILL.md` | Manually invoked understanding, debugging, review, and support-post workflows. |
| `.vscode/settings.json` | Disable inline completions and next-edit suggestions while retaining chat. |
| `.vscode/mcp.json` | Empty repository server list; no external service is required. |
| This directory | Activity sources, release checks, and the proposed instructor verification design. |

Repeat the short authorship boundary where discovery requires it, but keep
activity facts in the activity guide. A Markdown link does not guarantee a
client will load another file. Repository instruction formats and precedence
vary by client; do not promise universal enforcement.

## Configure a course release

1. Use the approved course and activity directions to resolve
   `{{AI TODO: ...}}` authoring fields. These markers are intentional in this
   source template. Do not invent outcomes, rubrics, support routes, commands,
   or answer content to make a field appear complete.
2. Update the course identity and actual activity set. When renaming, adding,
   or removing activity folders, update the `applyTo` patterns in the shared
   mentoring instructions and all related links and references.
3. Configure each activity's `AGENTS.md` from
   [the maintained source](activity/AGENTS.md.template). Supply outcomes,
   authoritative references, the selected scaffold level, protected outputs,
   original-work restrictions, and permitted student-run checks. Preserve
   the general mentoring boundary. The current six guides intentionally
   contain generic context until course creation supplies those facts.
4. Keep only the approved activity materials in the configured release.
   Alternative `.level*` and `.new` sources must not be interpreted as extra
   assignments or targets for AI completion.
5. Use [the optional activity adapter](activity/activity.instructions.md.template)
   only when an activity needs additional Copilot context or a supported
   client requires it. Place the configured file under `.github/instructions/`
   with a real `.instructions.md` suffix and a verified activity `applyTo`.
   Do not create six active copies of the shared policy without a need.
6. Keep all four manually invoked skills in `.github/skills/`, with each
   `SKILL.md` named for its containing folder. Preserve `user-invocable: true`
   and `disable-model-invocation: true` unless a separate release review
   explicitly authorizes a change. Skills do **not** select Course Mentor or
   restrict tool permissions; students must select the agent separately.
7. Remove source-only authoring sections from the released student documents
   and AI instructions, including literal placeholder examples and references
   to this authoring directory. Retain the authoring sources upstream and
   exclude `.github/ai-templates/` from the student release. Resolve all other
   authoring placeholders throughout the release; students must not receive
   `{{AI TODO: ...}}` markers or unresolved course context.
8. Preserve established course EOL rules in `.gitattributes`, `.editorconfig`,
   and editor settings. Do not normalize student submissions to a different
   policy while configuring AI support.
9. Run static validation and the manual
   [acceptance scenarios](acceptance-checks.md). Record the tested client,
   harness, model, settings, tool exposure, and remaining limitations outside
   the student instructions. Publish only after the course context and
   mentoring behavior have been reviewed.

The activity source's relative links target a top-level activity directory.
They are meant for the instantiated `AGENTS.md`, not for navigation from the
inactive `.md.template` source. Adjust those links if activities are nested
more deeply in a future course. The optional Copilot adapter's links target
its eventual `.github/instructions/` location. A `.template` suffix keeps
these sources from becoming active instruction files by default.

## Client behavior and maintenance

Select **Course Mentor** in a supported VS Code **Copilot harness** session
and inspect the tools actually exposed. Invoke one of the four skills using
`/understand-activity`, `/debug-my-attempt`, `/review-my-work`, or
`/draft-support-post`. The skills are explicitly invoked, not auto-selected;
unlike the former prompt files, they have no `agent` frontmatter setting and
cannot automatically switch to Course Mentor. Validate actual agent selection
and tool exposure. These slash commands are not guaranteed in GitHub.com Chat.

The read/search profile is a default mentoring configuration. An empty
workspace MCP list does not disable user-level servers, and workspace
settings do not prevent someone choosing other tools or customizations.
Instruction compliance and student authorship require more than file presence.
Do not describe this package as a technical guarantee against answer generation.

For authorized template maintenance, follow the root `AGENTS.md` validation
guidance. Keep the Course Mentor and skills aligned when changing names or
guidance. Review all active activity guides when changing their maintained
source; existing copies do not synchronize automatically.

The [instructor integrity-check design](instructor-integrity-plan.md) proposes
an external, read-only comparison against an instructor-controlled baseline.
It is a design only; this package does not install or activate a checker.

## Authoritative client references

- [GitHub custom instructions](https://docs.github.com/en/copilot/concepts/prompting-and-context/custom-instructions)
- [VS Code custom instructions](https://code.visualstudio.com/docs/agent-customization/custom-instructions)
- [VS Code custom agents](https://code.visualstudio.com/docs/agent-customization/custom-agents)
- [Custom agent file reference](https://code.visualstudio.com/docs/agents/reference/custom-agent-file-reference)
- [VS Code Agent Skills](https://code.visualstudio.com/docs/agent-customization/agent-skills)
- [VS Code prompt-to-skill migration](https://code.visualstudio.com/docs/agent-customization/migrate-customizations)
- [GitHub Copilot Agent Skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills)
- [Copilot inline suggestion settings](https://code.visualstudio.com/docs/editing/ai-powered-suggestions)
