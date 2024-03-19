#!/usr/bin/env python3
"""Module creates regular function syntax order than async function
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay) -> asyncio.Task:
    """This returns a asyncio.Task"""
    return asyncio.create_task(wait_random(max_delay))
