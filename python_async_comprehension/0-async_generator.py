#!/usr/bin/env python3
"""
This module defines an async generator that yields random numbers
with a 1-second asynchronous delay between each yield.
"""

import asyncio
import random


async def async_generator():
    """
    Asynchronously generates 10 random numbers between 0 and 10.

    Yields:
        float: random number between 0 and 10
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
