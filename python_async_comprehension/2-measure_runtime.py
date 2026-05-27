#!/usr/bin/env python3
"""Module that measures the runtime of four parallel async comprehensions."""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime of executing async_comprehension four times
    in parallel using asyncio.gather and return the elapsed time in seconds.
    """
    start = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    return time.perf_counter() - start
