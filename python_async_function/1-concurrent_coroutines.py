#!/usr/bin/env python3
"""Create a list of delayed times"""
import random
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """Call function n times"""
    i = 0
    delays = []
    while i < n:
        result = await wait_random(max_delay)
        delays.append(result)
        i += 1
    delays.sort()
    return delays
