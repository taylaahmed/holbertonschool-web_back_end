#!/usr/bin/env python3
"""Async Generator: function"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """for 10 times generate random number"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
