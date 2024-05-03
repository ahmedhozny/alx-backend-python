#!/usr/bin/env python3
"""
Floors a given float
"""


def floor(n: float) -> int:
    """
    Floors a given float
    Args:
        n (float): number to be floored.
    """
    return int(n) if n >= 0 else int(n) - 1
