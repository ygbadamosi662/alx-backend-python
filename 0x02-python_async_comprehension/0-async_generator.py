#!/usr/bin/env python3
"""
    Defines an async async_generator function
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
        async_generator: yields a randomly generated float.

    Returns:
        float: randomly generated float
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
