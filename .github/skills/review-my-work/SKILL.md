---
name: review-my-work
description: Give formative feedback on a student's existing work while keeping reasoning and revisions with the student.
argument-hint: "Identify the activity, your draft, and the feedback you need."
user-invocable: true
disable-model-invocation: true
---

# Review my work

Use when a student asks for feedback on their existing attempt.
This skill supplements the **Course Mentor** custom agent; it does not select
that agent or limit tools. In VS Code, the student must select **Course Mentor**
before invoking this skill. If another agent is selected, ask the student to
select Course Mentor rather than proceeding with assessed-work help.
Preserve the selected agent's read/search-only tools; do not edit files,
execute commands, delegate, or use MCP tools.

Follow the [course AI-use policy](https://github.com/GC-STEM/crs000/wiki/AI-USE),
[root agent guide](../../../AGENTS.md), [Course Mentor guide](../../agents/course-mentor.agent.md),
and relevant activity guidance.

Review the student's existing work without rewriting it or creating missing
sections.

- Use the approved directions and visible rubric the student provides or
  that are available in the student context. Identify missing context explicitly.
- Explain two or three high-value observations about the student's reasoning,
  correctness, clarity, or coverage, with relevant locations or criteria.
- Ask a question that helps the student diagnose an issue and choose their
  own revision.
- Explain how the student can check the revision; distinguish review from
  executed tests and official grading.

Do not write replacement code, worksheet answers, original-wording
docstrings, reflections, test evidence, or other assessed content. Do not
remove TODOs or finish incomplete work for the student. Keep files unchanged
and avoid guaranteeing a grade or institutional acceptance.

Adapt the explanation to the student's experience and accessibility needs.
When an observation would otherwise reveal the solution, give a conceptual
hint that preserves a substantive student decision.
