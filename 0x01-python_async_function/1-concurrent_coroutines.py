#!/usr/bin/env python3
"""
Asyncio basics
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns a wait_random n times with the specified max_delay
    and return the list of all the delays in ascending order.
    """
    delays = []
    for _ in range(n):
        delays.append(wait_random(max_delay))
    return sorted(await asyncio.gather(*delays))
