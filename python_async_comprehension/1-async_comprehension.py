#!/usr/bin/env python3
"""
This module collects 10 random numbers using async comprehension.
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using async comprehension over async_generator.

    Returns:
        List[float]: list of 10 random floats
    """

    return [value async for value in async_generator()]
