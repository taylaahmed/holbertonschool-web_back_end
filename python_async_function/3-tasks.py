#!/usr/bin/env python3
"""Task Wait Random: Function"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """Creating an asyncio Task"""
    return asyncio.create_task(wait_random(max_delay))
