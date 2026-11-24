"""Instructor-provided learning checks for the Higher/Lower Game.

Run from the repository root:
    python 1-3_Example_Activity/tests/test_high_low.py

The incomplete starter is expected to fail. These checks do not grade work.
Review feedback messages manually using docs/40_testing.md.
"""

import importlib.util
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from unittest.mock import patch


ACTIVITY_ROOT = Path(__file__).resolve().parents[1]
PROGRAM_PATH = ACTIVITY_ROOT / "src" / "high_low.py"


def load_program():
    """Load the starter without running its interactive main guard."""
    spec = importlib.util.spec_from_file_location("high_low", PROGRAM_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Could not load src/high_low.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class HigherLowerGameChecks(unittest.TestCase):
    """Check selected input and random-selection behavior, not message text."""

    def check_game(self, inputs, secret, bounds):
        """Check input use and target creation with controlled values."""
        module = load_program()
        self.assertTrue(
            callable(getattr(module, "main", None)),
            "Keep the provided main() wrapper.",
        )
        self.assertTrue(
            hasattr(module, "randint"),
            "Keep the provided 'from random import randint' import.",
        )
        output = StringIO()
        with (
            patch(
                "builtins.input",
                side_effect=[str(value) for value in inputs],
            ) as fake_input,
            patch.object(module, "randint", return_value=secret) as fake_random,
            redirect_stdout(output),
        ):
            try:
                module.main()
            except StopIteration:
                self.fail(
                    "The program requested more input than this case provides. "
                    "Review repeated prompts and stopping behavior."
                )

        fake_random.assert_called_once_with(*bounds)
        self.assertEqual(
            fake_input.call_count,
            len(inputs),
            "Expected all inputs to be used and no extra guess after success.",
        )

    def test_t01_valid_bounds_and_immediate_success(self):
        self.check_game([10, 20, 17], secret=17, bounds=(10, 20))

    def test_t02_reversed_bounds(self):
        self.check_game([10, 5, 10, 20, 17], secret=17, bounds=(10, 20))

    def test_t03_equal_bounds(self):
        self.check_game([10, 10, 10, 20, 17], secret=17, bounds=(10, 20))

    def test_t04_guesses_outside_both_bounds(self):
        self.check_game([10, 20, 9, 21, 17], secret=17, bounds=(10, 20))

    def test_t05_invalid_guess_after_valid_guess(self):
        self.check_game([10, 20, 15, 21, 17], secret=17, bounds=(10, 20))

    def test_t06_incorrect_guesses_before_success(self):
        self.check_game([10, 20, 15, 19, 17], secret=17, bounds=(10, 20))

    def test_t07_lower_endpoint(self):
        self.check_game([10, 20, 10], secret=10, bounds=(10, 20))

    def test_t07_upper_endpoint(self):
        self.check_game([10, 20, 20], secret=20, bounds=(10, 20))

    def test_t08_negative_bounds_and_zero(self):
        self.check_game([-5, 0, -3], secret=-3, bounds=(-5, 0))


if __name__ == "__main__":
    unittest.main(verbosity=2)
