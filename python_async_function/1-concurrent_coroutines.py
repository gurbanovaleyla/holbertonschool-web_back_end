#!/usr/bin/env python3
"""
This module runs multiple asynchronous coroutines concurrently and returns
their execution times in ascending order.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the given max_delay and returns
    the list of delays in ascending order.

    Args:
        n (int): number of coroutines to spawn
        max_delay (int): maximum delay for each coroutine

    Returns:
        List[float]: list of delays in ascending order
    """
    tasks = []

    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    results = []

    for task in asyncio.as_completed(tasks):
        result = await task
        results.append(result)

    return results
