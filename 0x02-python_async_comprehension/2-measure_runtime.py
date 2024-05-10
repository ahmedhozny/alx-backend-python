#!/usr/bin/env python3
"""
Measure runtime of async_comprehension usage
"""

import asyncio
from time import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Measures runtime of async_comprehension usage
    """
    start_time = time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time() - start_time
