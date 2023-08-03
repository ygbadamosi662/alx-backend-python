#!/usr/bin/env python3
"""
    Defines the sum_list function
"""
from typing import List
from functools import reduce


def sum_list(input_list: List[float]) -> float:
    """
        sum_list: return the sum of the list in float.

        Args:
            input_list (list[float]): list with only float as parameters

        Returns:
            float: the sum of the list in float
    """
    return reduce(lambda x, y: x + y, input_list)
