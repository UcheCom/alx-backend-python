#!/usr/bin/env python3
"""Module returns list of tuples containing the element and its length"""
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Returns a list of tuples where each tuple contains
    an element from the input list and its length.

    Args:
        lst (List[str]): The input list of strings.
    """
    return [(i, len(i)) for i in lst]
