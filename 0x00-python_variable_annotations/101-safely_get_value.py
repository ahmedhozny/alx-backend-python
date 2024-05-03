#!/usr/bin/env python3
"""
Return the first element of a sequence if available.
"""

from typing import Any, Sequence, Union, Mapping, TypeVar

T = TypeVar('T')
Default = Union[T, None]
Res = Union[Any, T]

def safely_get_value(dct: Mapping, key: Any, default: Default) -> Res:
    """
    Returns the first element of a sequence if available.
    Args:
        dct (Mapping): The sequence to check.
        key (Any): The key to check.
        default (Default): The value to return if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
