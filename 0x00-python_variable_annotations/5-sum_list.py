#!/usr/bin/env python3
"""
Sum all values in a list
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sums all values in a list.
    Args:
        input_list (List[float]): list of numbers
    """
    return float(sum(input_list))
