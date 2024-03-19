#!/usr/bin/env python3
"""Module measure_runtime coroutine that will execute
async_comprehension four times in parallel using asyncio.gather
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime and return it"""
    start = time.perf_counter()
    task = [async_comprehension() for i in range(4)]
    await asyncio.gather(*task)
    end = time.perf_counter()
    return (end - start)
