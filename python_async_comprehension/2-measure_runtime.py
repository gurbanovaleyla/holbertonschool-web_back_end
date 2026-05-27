#!/usr/bin/env python3
"""
This module measures the runtime of running
four async comprehensions in parallel.
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times
    in parallel and measures total runtime.

    Returns:
        float: total execution time in seconds
    """

    start_time = time.time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.time()

    return end_time - start_time
