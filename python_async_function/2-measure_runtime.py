#!/usr/bin/env python3
"""
This module measures the average runtime of concurrent coroutines.
"""

import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average execution time of wait_n(n, max_delay).

    Args:
        n (int): number of coroutines to run
        max_delay (int): maximum delay for each coroutine

    Returns:
        float: average time per coroutine
    """

    start_time = time.time()

    wait_n(n, max_delay)

    end_time = time.time()

    return (end_time - start_time) / n
