#!/usr/bin/env python3
"""
Module takes a list mxd_lst of integers and floats and
returns their sum as a float.
"""
from typing import Union


def sum_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
    """Returns their sum as a float"""
    return sum(mxd_lst)
