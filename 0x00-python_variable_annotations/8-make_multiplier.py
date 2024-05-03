#!/usr/bin/env python3
"""
Takes a float multiplier and returns a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float multiplier and returns a multiplier function.
    Args:
        multiplier (float): The multiplier value.
    """
    return lambda x: x * multiplier
