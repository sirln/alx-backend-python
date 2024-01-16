#!/usr/bin/env python3
"""
New async function module
"""

import asyncio
from typing import List

task_wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Async routine that spawns task_wait_random n times
    with the specified max_delay.

    Parameters:
    - n (int): The number of times to spawn task_wait_random.
    - max_delay (int): The maximum delay in seconds.

    Returns:
    - List[float]: The list of delays in ascending order.
    """
    # Create a list to store the delays
    delays = []

    tasks = [task_wait_random(max_delay) for _ in range(n)]

    results = await asyncio.gather(*tasks)

    delays.extend(results)

    return (delays.sort())
