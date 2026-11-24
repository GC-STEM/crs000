# 1-3 Higher/Lower Game | Software Requirements Specification

**Status:** Instructor-provided reference; do not edit during student work.

## Purpose and Scope

Define the behavior of the Python game in this demonstration. The source
activity is IT 140 Module Four, but its pseudocode deliverable and rubric are
not the deliverable or rubric for this adaptation. This document defines the
demonstration requirements; it does not revise the official course assignment.

## Functional Requirements

| ID | Required behavior |
| --- | --- |
| FR-001 | Prompt for integer lower and upper bounds. |
| FR-002 | Require the lower bound to be less than the upper bound. Explain invalid bounds and request both bounds again until valid. |
| FR-003 | Select one random integer within the valid range, including either endpoint, and retain it for the game. |
| FR-004 | Prompt for an integer guess within the selected range. |
| FR-005 | Reject a guess below the lower bound or above the upper bound, explain that it is outside the range, and request another guess. |
| FR-006 | For a valid guess, distinguish too low, too high, and correct, and display appropriate feedback. |
| FR-007 | Continue accepting and validating guesses after each incorrect guess. |
| FR-008 | End after the correct guess and success feedback, without requesting another guess or starting another round. |

## Quality Requirements

- Use understandable prompts and messages. Exact message wording is not graded
  or enforced by the supplied checks.
- Use meaningful names, readable indentation, and comments that explain intent.
- Keep the program simple and consistent with the concepts listed in the README.

## Technology and File Constraints

- The sole required deliverable is `src/high_low.py`.
- Use Python 3.12 and the standard library; keep `from random import randint`.
- Keep the supplied `main()` wrapper and main guard. No additional functions,
  classes, packages, files, or services are required.
- Students write their implementation and explanatory docstrings themselves.
  Sources used must be acknowledged in the source file's References comments.
- Pseudocode, a diagram, and the worksheet are optional planning aids.

## Assumptions and Out of Scope

Inputs are integer text, including zero and negative integers when appropriate.
Handling letters, decimal text, blank input, or end-of-input is outside this
example's required behavior. No guess limit, counter, score, replay, GUI, or
persistent storage is required.

Inclusive endpoints, requesting both bounds again after invalid bounds, and
retaining one target per game are explicit conventions for this Python
demonstration. They are not claims about additional official rubric criteria.

## Acceptance Criteria and Traceability

| Requirement | Design guidance | Implementation | Verification |
| --- | --- | --- | --- |
| FR-001, FR-002 | [Validation](20_design.md#validation-and-repetition) | `src/high_low.py` | T-01, T-02, T-03; prompt/message review |
| FR-003 | [Provided structure](20_design.md#architecture-overview) | `src/high_low.py` | T-01 through T-08 check random-operation arguments and call count |
| FR-004, FR-005 | [Validation](20_design.md#validation-and-repetition) | `src/high_low.py` | T-04, T-05; invalid-input feedback review |
| FR-006 | [Decisions](20_design.md#decisions-and-feedback) | `src/high_low.py` | T-06 plus manual feedback review |
| FR-007, FR-008 | [Validation](20_design.md#validation-and-repetition) | `src/high_low.py` | T-01, T-04 through T-08; stopping review |

See [the test plan](40_testing.md) for cases and coverage limits. Automated
results are learning feedback, not a grade. No new grading weights or
institutional submission rules are defined here.

## Source

Adapted from the instructor-provided
[IT 140 Module Four requirements](https://github.com/GC-STEM/it140-m4-assignment/blob/main/analysis/hilow_game_srs.md).
The old filename occurs only in this source reference.
