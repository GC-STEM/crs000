# 1-3 Higher/Lower Game | Software Solution Overview

**Status:** Instructor-provided reference; not a student deliverable.

## Problem or Need

A player wants to guess a secret number within a range they choose. The game
must explain whether a valid guess is too low, too high, or correct.

## Solution Purpose

Create a small console program that lets a player keep guessing until they
find the secret number. This activity gives beginning programmers practice
with input, decisions, validation, and repetition.

## Users and Stakeholders

| Stakeholder | Need |
| --- | --- |
| Player | Clear prompts and feedback; invalid ranges and guesses handled. |
| Student developer | Requirements and checks that support independent work. |
| Instructor | A Python deliverable and an activity for demonstrating AI mentoring. |

## Solution Overview

The player enters integer bounds and guesses. The program chooses a secret
integer in the valid range and provides feedback. A correct guess ends the game.

| Category | Description |
| --- | --- |
| Inputs | Lower bound, upper bound, and each guess, entered in the terminal. |
| Processing | Range validation, random selection, comparison, and repetition. |
| Outputs | Prompts, validation feedback, high/low feedback, and success feedback. |

## Assumptions and Constraints

The program uses Python 3.12 and the standard library. Both range endpoints
are included. Input can be assumed to be integer text. The program has one
player and one round, with no network, stored scores, or graphical interface.

## Success Criteria

All required behavior in the [requirements](10_requirements.md) is present in
the student's [Python source](../src/high_low.py), and the student can explain
their implementation and observed test results.

## Related Documents

- [Requirements](10_requirements.md)
- [Design](20_design.md)
- [Architecture](21_architecture.md)
- [Construction](30_construction.md)
- [Testing](40_testing.md)
- [Optional worksheet](worksheet.md)
