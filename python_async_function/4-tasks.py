#!/usr/bin/env python3
"""Task Wait N: function"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """create tasks for functions"""
    i = 0
    delays = []
    while i < n:
        result = await task_wait_random(max_delay)
        delays.append(result)
        i += 1
    delays.sort()
    return delays
