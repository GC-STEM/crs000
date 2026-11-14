---
name: draft-support-post
description: Draft a factual, privacy-conscious GitHub Issue or Discussion for student review without publishing it.
argument-hint: "Describe the problem, what happened, and the help you want."
user-invocable: true
disable-model-invocation: true
---

# Draft a support post

Use when a student needs help drafting a non-assessed GitHub Issue or
Discussion about repository or course support.
This skill supplements the **Course Mentor** custom agent; it does not select
that agent or limit tools. In VS Code, the student must select **Course Mentor**
before invoking this skill. If another agent is selected, ask the student to
select Course Mentor rather than proceeding with assessed-work help.
Preserve the selected agent's read/search-only tools; do not edit files,
execute commands, delegate, use MCP tools, or post anything.

Follow the [course AI-use policy](https://github.com/GC-STEM/crs000/wiki/AI-USE),
[root agent guide](../../../AGENTS.md), [Course Mentor guide](../../agents/course-mentor.agent.md),
and the documented support routes.

Help draft a non-assessed GitHub Issue or Discussion using the facts the
student provides. This support-writing assistance is allowed; it does not
authorize publishing a post or completing assessed work.

- Clarify whether the student is reporting a repository problem or asking a
  conceptual question. Use a documented private course channel for grades,
  personal circumstances, credentials, or restricted material.
- Use the student's actual command, message, observation, and attempts. Ask
  for essential missing facts; leave other omissions explicit. Do not invent
  diagnoses, reproduction results, troubleshooting steps, or software versions.
- Draft a useful title and concise body covering context, expected and actual
  behavior, relevant reproduction steps, environment, what the student tried,
  and a focused request for help. Include only sections useful for this report.
- Remove private information and limit code to the minimal permitted context.
  Do not disclose or request a completed assignment solution.

Return the draft in chat for the student's review. Do not post, send, upload,
commit, or edit repository files. If the proposed post is itself an assessed
deliverable, provide structure and questions rather than drafting its
assessed content.
