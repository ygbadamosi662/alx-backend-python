#!/usr/bin/env python3
"""
    Defines an async measure_runtime function
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
        measure_runtime: returns the total time taken for async to complete.

        Returns:
            float: this return value will be between 10 and 10.2. This is due
            to the fact that the generator waited 1 second after yield and the
            yielded 10 times.
    """
    tasks = [async_comprehension()] * 4
    starts = time.perf_counter()
    await asyncio.gather(*tasks)

    return time.perf_counter() - starts
