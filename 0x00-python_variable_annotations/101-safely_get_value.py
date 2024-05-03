#!/usr/bin/env python3
"""
Return the first element of a sequence if available.
"""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a sequence if available.
    Args:
        lst (Sequence[Any]): The sequence to check.
    """
    return lst[0] if lst else None
