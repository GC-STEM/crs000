# 1-3 Higher/Lower Game | Software Design Description

**Status:** Instructor-provided design guidance; not a completed game design or a student deliverable.

## Purpose and Scope

Use the [requirements](10_requirements.md) to plan your own implementation before coding. This document describes the program's overall structure and identifies design questions without supplying the game's algorithm.

## Design Inputs

Read the [requirements](10_requirements.md) and review the [Python starter](../src/high_low.py).

Optional spaces for your own planning are the [worksheet](worksheet.md), [pseudocode scratchpad](26_pseudocode.txt), and [diagram canvas](23_diagram.drawio). None is an additional submission.

## Architecture Overview

The program runs as a single Python process and interacts with one player through a terminal. It uses no network, database, graphical interface, or saved game state.

| Element | Responsibility |
| --- | --- |
| Terminal | Accept player input and display messages. |
| [src/high_low.py](../src/high_low.py) | Hold your game implementation. |
| Python standard library | Supply the random integer operation. |
| [tests/test_high_low.py](../tests/test_high_low.py) | Check selected behaviors using controlled input and random values. |

One source file and one supplied starting point keep the program small and easy to run. Terminal interaction supports practice with input and output. No additional framework or infrastructure is needed.

## Provided Structure

The starter includes `from random import randint`, a `main()` function, and a main guard.

- **Import:** Makes the standard library's `randint` operation available.
- **`main()` function:** Groups the statements that run your game.
- **Main guard:** Calls `main()` when you run the file directly.

Keep this supplied structure and write your game inside `main()`. You do not need to define additional functions or classes.

This structure also lets the provided tests load the file without starting an interactive game. The tests then call `main()` with controlled inputs and random values. The testing code uses techniques you are not required to use in your game.

## Environment and Dependencies

Use Python 3.12 in the STEM Standard Operating Environment (SOE) or course environment, locally or in Codespaces.

The program and its provided learning checks need only Python's standard library. No additional packages are required.

## Data and Interfaces

Decide which values your program must remember, what each value means, and where it comes from.

The player enters integer text in the terminal, and the program displays prompts and feedback there. The supplied `randint` operation accepts valid lower and upper bounds and returns an integer that can include either endpoint.

The program does not read or write data files. Game values remain in memory while the program runs.

## Validation and Repetition

For each input rule, consider what makes the input valid and how the player can try again.

For each loop you design, identify:

- What condition causes repetition?
- What information can change during a repetition?
- What allows the loop to end?

Consider invalid input during later guesses as well as at the start. Follow the integer-input assumption and validation requirements in the [requirements document](10_requirements.md).

## Decisions and Feedback

Range validation and comparison with the secret number answer different questions. Explain that distinction in your own words.

Decide how your program will communicate each required outcome while keeping the secret number unchanged throughout the game.

## Design Verification and Traceability

Choose one case from the [test plan](40_testing.md) and trace your own design by hand. Compare the behavior you predict with the related requirements.

Use your optional worksheet to record decisions, gaps, or questions. Confirm that your design addresses each functional requirement, then use the [construction guidance](30_construction.md) to implement it.

Revise your design when testing reveals a problem. The required deliverable remains `src/high_low.py`; this design document is a reference.
