# 1-3 Higher/Lower Game | Software Test Plan

**Status:** Instructor-provided plan; observations must come from actual runs.

## Purpose and Scope

Check [`src/high_low.py`](../src/high_low.py) against the
[requirements](10_requirements.md). Review range validation, random selection,
feedback, repeated guesses, and stopping behavior.

Nonnumeric input, replay, scoring, and exact message wording are out of scope.

## Test Environment and Tools

Use Python 3.12. From the **repository root**, run:

```bash
python 1-3_Example_Activity/tests/test_high_low.py
```

The checks use only the standard library. They substitute a known secret and
input values so repeated runs can check the same behavior. They do not require
a student to learn the test harness's advanced Python features.

## Test Cases and Requirements Traceability

Input sequences below list lower bound, upper bound, and subsequent inputs.
For invalid bounds, the next two values are replacement bounds.

| ID | Inputs | Controlled secret | Expected behavior | Requirements |
| --- | --- | --- | --- | --- |
| T-01 | 10, 20, 17 | 17 | Use valid bounds and stop after the first correct guess. | FR-001, FR-003, FR-004, FR-008 |
| T-02 | 10, 5, 10, 20, 17 | 17 | Reject reversed bounds, request both again, then play. | FR-001, FR-002, FR-003 |
| T-03 | 10, 10, 10, 20, 17 | 17 | Reject equal bounds, request both again, then play. | FR-002, FR-003 |
| T-04 | 10, 20, 9, 21, 17 | 17 | Reject guesses below and above the range; accept the correct guess. | FR-004, FR-005, FR-007, FR-008 |
| T-05 | 10, 20, 15, 21, 17 | 17 | Validate a later guess after an incorrect valid guess. | FR-005, FR-007, FR-008 |
| T-06 | 10, 20, 15, 19, 17 | 17 | Continue through too-low and too-high guesses, then stop. | FR-006, FR-007, FR-008 |
| T-07 | 10, 20, 10; separately 10, 20, 20 | 10; separately 20 | Accept either endpoint as the correct guess. | FR-003, FR-005, FR-008 |
| T-08 | -5, 0, -3 | -3 | Support a valid range containing negative integers and zero. | FR-001, FR-003, FR-004, FR-008 |

## Manual Review

The automated checks verify use of the selected bounds, one random selection,
and the number of inputs consumed. They do **not** verify all prompt text,
feedback meaning, internal validation logic, or code quality. A program may
consume the right number of inputs while giving incorrect feedback.

Run the interactive game and inspect invalid-bound, out-of-range, too-low,
too-high, and success messages. Confirm that invalid guesses receive range
feedback rather than ordinary high/low feedback. Confirm the target remains
unchanged and the program ends after success. In a manual run, the secret is
random; do not assume it is the controlled value in the table. Use output and
code review to confirm the decisions, and use the harness for repeatable inputs.

## Pass / Fail Criteria

A case passes when its observed behavior matches the requirement. Automated
passes alone do not establish full correctness or a grade. The untouched
starter is expected to fail; do not change the tests to obtain a pass.

If a run asks for unexpected extra input, the harness may report
`StopIteration`. That means its supplied input sequence was exhausted; review
the prompts and stopping behavior. If a run never ends, stop it with Ctrl+C
and investigate a loop that does not make progress.

## Test Evidence and Reproducibility

Optionally record cases, expected and actual behavior, and follow-up notes in
[the worksheet](worksheet.md). Leave observations blank until you run a case.
Keep test evidence factual. After a correction, rerun the affected case and
the learning checks to look for unintended changes. Do not invent a pass.
