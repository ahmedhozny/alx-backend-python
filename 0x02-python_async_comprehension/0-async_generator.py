#!/usr/bin/env python3
"""
Generate a sequence of 10 numbers using a generator function.
"""

import asyncio
from random import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Generates a sequence of 10 numbers.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random() * 10
