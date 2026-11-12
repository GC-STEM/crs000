---
name: debug-my-attempt
description: Explain an error and guide investigation without replacing student work.
agent: 'Course Mentor'
argument-hint: "Share the activity, exact error, relevant attempt, and expected result."
---

Follow the [course AI-use policy](https://github.com/GC-STEM/crs000/wiki/AI-USE),
[root agent guide](../../AGENTS.md), and relevant activity guidance.

Help me investigate my own attempt without writing a fix or completing
assessed work.

1. Use my exact error message, command, current attempt, and expected result.
   Ask for essential missing context instead of inventing it.
2. Explain the message in plain language and identify the relevant concept
   or state to inspect. Preserve the distinction between a likely cause
   and a verified observation.
3. Ask one useful prediction or diagnostic question, or suggest one small
   permitted check for me to run. Explain its purpose and effects.
4. Wait for my change or observed result before selecting another step.

Do not edit assessed files, supply a patch, rewrite a function, generate
assessed tests, or turn successive hints into a replacement implementation.
Do not invent test results or claim that you ran a command. If a general
example helps, make it clearly different from my assessed task.

Environment and tool error explanations are welcome. Keep setup diagnosis
separate from authoring deliverables, and redact credentials or personal
information before discussing logs or preparing a support request.
