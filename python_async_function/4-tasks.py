#!/usr/bin/env python3
"""
This module runs multiple asyncio Tasks concurrently and returns
their results in order of completion.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times and returns the list of delays
    in ascending order based on completion time.

    Args:
        n (int): number of tasks to spawn
        max_delay (int): maximum delay for each task

    Returns:
        List[float]: list of delays in completion order
    """

    tasks = []

    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    results = []

    for task in asyncio.as_completed(tasks):
        result = await task
        results.append(result)

    return results
