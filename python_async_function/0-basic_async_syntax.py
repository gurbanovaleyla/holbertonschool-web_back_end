#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine that waits for a random delay
and returns that delay value.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay seconds and returns it.

    Args:
        max_delay (int): Maximum delay in seconds (default is 10).

    Returns:
        float: The randomly generated delay value.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
