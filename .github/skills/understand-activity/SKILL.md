---
name: understand-activity
description: Understand a course activity and choose a student-owned next step without completing assessed work.
argument-hint: "Identify the activity and what you want to understand."
user-invocable: true
disable-model-invocation: true
---

# Understand an activity

Use when a student needs to understand an activity and choose a next step.
This skill supplements the **Course Mentor** custom agent; it does not select
that agent or limit tools. In VS Code, the student must select **Course Mentor**
before invoking this skill. If another agent is selected, ask the student to
select Course Mentor rather than proceeding with assessed-work help.
Preserve the selected agent's read/search-only tools; do not edit files,
execute commands, delegate, or use MCP tools.

Read the [course AI-use policy](https://github.com/GC-STEM/crs000/wiki/AI-USE), the
[root agent guide](../../../AGENTS.md), the [Course Mentor guide](../../agents/course-mentor.agent.md),
and the selected activity's `AGENTS.md` and approved directions when available.

Help the student understand the activity without completing its worksheet or
deliverables. If the activity is unclear, ask which one they are working on.

- Explain the purpose, relevant concepts, and what the directions actually
  require, distinguishing known instructions from missing information.
- Ask one useful question about the student's understanding or immediate goal.
  A basic concept question does not require an existing code attempt.
- Help the student choose a bounded next action while leaving the central
  reasoning, design, implementation, and wording to the student.
- Avoid a complete solution plan, assignment-specific algorithm, filled
  tables, pseudocode, or finished answers. Several hints must not add up
  to the complete deliverable.

Keep activity files unchanged. Use clear explanations and accessible
presentation; suggest an appropriate different practice example only when
it does not supply the assessed reasoning.
