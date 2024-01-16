#!/usr/bin/env python3
"""
Async function module
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task for the wait_random
    coroutine with the specified max_delay.

    Parameters:
    - max_delay (int): The maximum delay in seconds.

    Returns:
    - asyncio.Task: The asyncio.Task for wait_random.
    """

    # asyncio event loop
    loop = asyncio.get_event_loop()

    task = loop.create_task(wait_random(max_delay))

    return (task)
