#!/usr/bin/env python3
"""
Module writes coroutine called async_generator that takes no arguments.
"""
import random
import asyncio


async def async_generator():
    """The coroutine will loop 10 times, each time
    asynchronously wait 1 second
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
