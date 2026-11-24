# 1-3 Example Activity | Higher/Lower Game

Build a Python number-guessing game. The player chooses a range, guesses a
random number in that range, and receives feedback until the guess is correct.

**Required deliverable:** [`src/high_low.py`](src/high_low.py).

This demonstration adapts the IT 140 Module Four game to a Python deliverable.
It does not replace the official Module Four assignment, which uses pseudocode.
No grading weights, deadline, or Brightspace submission destination are assigned
to this demonstration. If your instructor assigns it, follow their submission
directions.

## Learning Goals and Prerequisites

Practice interpreting requirements, using input/output, making decisions,
writing while loops, validating ranges, and checking program behavior.
Before starting, review variables, integer conversion, comparisons, Boolean
expressions, indentation, and `if`/`elif`/`else`.

Use Python 3.12 in the course environment. The starter supplies a `main()`
wrapper and a main guard, which runs that wrapper when you run the file.
Keep these supplied parts; you do not need to write additional functions or
classes. The standard-library `randint` operation is also provided.

## Activity Files

| File | Role | Student action |
| --- | --- | --- |
| [src/high_low.py](src/high_low.py) | Required Python deliverable | Write and test your own implementation. |
| [docs/00_overview.md](docs/00_overview.md) | Problem and scope | Read. |
| [docs/10_requirements.md](docs/10_requirements.md) | Required behavior and constraints | Read and check your work against it. |
| [docs/20_design.md](docs/20_design.md) | Design guidance | Read; make your own design decisions. |
| [docs/30_construction.md](docs/30_construction.md) | Coding guidance | Read. |
| [docs/40_testing.md](docs/40_testing.md) | Test plan | Run checks and observe results. |
| [docs/worksheet.md](docs/worksheet.md) | Optional working notes | Write your own notes; not submitted. |
| [docs/26_pseudocode.txt](docs/26_pseudocode.txt) | Optional pseudocode scratchpad | Use if helpful; not submitted. |
| [docs/23_diagram.drawio](docs/23_diagram.drawio) | Optional diagram canvas | Use if helpful; not submitted. |
| [tests/test_high_low.py](tests/test_high_low.py) | Instructor-provided learning checks | Run; do not change to make your code pass. |

The numbered Markdown documents, README files, tests, AI guidance, and
configuration are course-managed references. Only the Python source is the
required deliverable. Optional planning files are not extra assignments.

## Complete the Activity

1. Read the overview and requirements. Explain the required behavior in your
   own words.
2. Use the design guidance to plan your solution. The worksheet, pseudocode,
   and diagram are optional ways to record your own thinking.
3. Implement your design in `src/high_low.py`. Work on one small part at a time.
4. Run the program and use the test plan. Correct your implementation based
   on what you observe.
5. Review the requirements and remove completed starter TODO prompts from
   `high_low.py`. Cite sources you used in its References comments, following
   any course-specific citation and AI-disclosure directions.

From the **course repository root**, run:

```bash
python 1-3_Example_Activity/src/high_low.py
```

Run the instructor-provided automated checks from the same directory:

```bash
python 1-3_Example_Activity/tests/test_high_low.py
```

Use the environment's Python 3.12 interpreter; if it is named `python3`,
substitute that command. The untouched starter does not play a game and will
fail the behavioral checks. Passing checks does not establish a grade or
replace manual review. Save, commit, and push only to your personal course
repository using the course setup directions; pushing does not submit work.

## Get Help With Copilot

Open the **whole course repository** in local VS Code or VS Code in Codespaces
so its AI guidance and settings are available. Select **Course Mentor** when
available and ask about this activity. On GitHub.com, select the repository as
context and open or attach the relevant activity files. Remote clients see only
the version available in their checkout or on GitHub.

Try: "I'm working on 1-3_Example_Activity. Read its README, AGENTS.md, and
docs/10_requirements.md. What am I expected to submit?"

You can also ask about a concept, share an error, or request feedback on your
own attempt. Copilot should explain and guide your next step while leaving the
code and reasoning to you. It should not complete the program or fill planning
files with its solution. A linked file is not necessarily loaded into chat;
add missing context when needed.

Read the [AI-use guidance](https://github.com/GC-STEM/crs000/wiki/AI-USE).
Use [course support](../README.md#help-and-support) for other help, and report
repository problems through [GitHub Issues](https://github.com/GC-STEM/crs000/issues).
Keep personal information and completed solutions out of public support posts.
