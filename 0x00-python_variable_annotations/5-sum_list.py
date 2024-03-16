#!/usr/bin/env python3
"""Module takes a list of floats as input and returns their sum as a float"""
from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of floats in the input list.

    Parameters:
        input_list (list[float]): The list of floats.
    """
    return sum(input_list)
