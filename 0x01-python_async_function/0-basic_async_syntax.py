#!/usr/bin/env python3
"""
    Defines an async wait_random function
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
        wait_random: this returns a random float value after waiting for it.

        Args:
            max_delay (int): maximum delay

        Returns:
            float: the ramdom generated value
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
