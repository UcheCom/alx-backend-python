#!/usr/bin/env python3
"""Module Create a measure_time function with integers n and max_delay
as arguments that measures the total execution time for wait_n(n, max_delay)
"""
import asyncio
from time import perf_counter
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n, max_delay) -> float:
    """This measures the runtime
    Args:
        n: the number of coroutines to launch
        max_delay: the maximum amount of time to wait for each coroutine
    """
    s = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elasped = perf_counter() - s
    return elasped / n
