#!/usr/bin/env python3
"""
    Defines the to_kv function
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float | int]:
    """
        to_kv: returns a tuple of string as first value and sq if int or
        float as second value.

    Args:
        k (str): string parameter
        v (Union[int, float]): integer or float parameter

    Returns:
        Tuple[str, float]: string ad=nd int/float
    """
    return tuple(k, v**2)
