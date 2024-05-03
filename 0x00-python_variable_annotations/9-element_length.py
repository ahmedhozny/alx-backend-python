#!/usr/bin/env python3

"""
Annotate the function parameters and return values with appropriate types.
"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculates the length of elements in the input list and returns a list
    of tuples where each tuple contains the original element and its length.

    Args:
        lst (Iterable[Sequence]): The input list of sequences.
    """
    return [(i, len(i)) for i in lst]
