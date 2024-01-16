#!/usr/bin/env python3
"""
Basic async module
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Async routine that spawns wait_random n times
    with the specified max_delay.

    Parameters:
    - n (int): The number of times to spawn wait_random.
    - max_delay (int): The maximum delay in seconds.

    Returns:
    - List[float]: The list of delays in ascending order.
    """

    # store delays
    delays = []

    # spawn wait_random n times asynchronously
    tasks = [wait_random(max_delay) for _ in range(n)]

    # use asyncio.gather to wait for all tasks to complete
    results = await asyncio.gather(*tasks)

    # add/append the delays to list
    delays = sorted(results)

    return (delays)
