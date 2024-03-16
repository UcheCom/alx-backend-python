#!/usr/bin/env python3
"""Module takes a float multiplier as argument and returns
a function that multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the specified multiplier

    Args:
        multiplier (float): The multiplier to use.
    """
    def multiplier_func(y: float) -> float:
        """Multiplies a float by multiplier"""
        return y * multiplier
    return multiplier_func
