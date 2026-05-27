#!/usr/bin/env python3
"""
This module creates an asyncio Task from the wait_random coroutine.
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task that runs wait_random.

    Args:
        max_delay (int): maximum delay for wait_random

    Returns:
        asyncio.Task: scheduled asynchronous task
    """

    return asyncio.create_task(wait_random(max_delay))
