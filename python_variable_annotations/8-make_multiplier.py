#!/usr/bin/env python3
"""Returns a function that multiplies a float by a multiplier."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies its input by multiplier."""
    def multiply(x: float) -> float:
        return x * multiplier
    return multiply
