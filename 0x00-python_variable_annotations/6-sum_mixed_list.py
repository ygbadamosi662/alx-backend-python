#!/usr/bin/env python3
"""
    Defines the sum_mixed_list function
"""
from typing import List, Union
from functools import reduce


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """
        sum_mixed_list

        Args:
            mxd_lst (List[int  |  float]): List with int and float

        Returns:
            float: sum in float
    """
    return reduce(lambda x, y: x + y, mxd_lst)
