#!/usr/bin/env python3
"""Module writes a coroutine called async_comprehension
that takes no arguments
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """The coroutine collects 10 random numbers using an async"""
    result = [num async for num in async_generator()]
    return result
