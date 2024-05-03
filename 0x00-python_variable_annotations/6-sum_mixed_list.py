#!/usr/bin/env python3
"""
Sum all values in a list
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums all values in a list.
    Args:
        mxd_lst (List[Union[int, float]]): list of numbers (floats and ints)
    """
    return float(sum(mxd_lst))
