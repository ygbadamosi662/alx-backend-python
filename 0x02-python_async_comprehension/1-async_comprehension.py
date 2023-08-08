"""
    Defines an async async_comprehension function
"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
        async_comprehension: returns a list of floats collected from a
        generator.

        Returns:
            List[float]: list of floats generated randomly between 0 and 10
    """
    return [i async for i in async_generator()]
