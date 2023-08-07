#!/usr/bin/env python3
"""
    Defines a measure_time function
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
        measure_time: returns the average time taken to finish the process.

        Args:
            n (int): the number of times the function will run
            max_delay (int): the maximum time the function will sleep

        Returns:
            int: returns the average time.
    """
    starts = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    exec_time_total = time.perf_counter() - starts

    return exec_time_total / n
