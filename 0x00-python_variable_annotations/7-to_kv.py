#!/usr/bin/env python3
"""Module takes a string k and an int OR float v
as arguments and returns a tuple."""


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    """
    Returns a tuple with the string k as the first
    element and the square of the int or float v as the second element.

    Parameters:
        k (str): The string.
        v (Union[int, float]): The integer or float.
    """
    return k, float(v ** 2)
