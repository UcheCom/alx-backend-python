#!/usr/bin/env python3
"""Module writes an async routine called wait_n that
takes in 2 int arguments (in this order): n and max_delay
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay) -> List[float]:
    """Returns list of all the delay(float values)
      Args:
           n: number of times to spawn wait_random
           max_delay: maximum delay between each call
    """
    tasks = [asyncio.create_t(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]

