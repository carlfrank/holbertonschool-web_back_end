#!/usr/bin/env python3
"""Module for async_generator coroutine"""

import asyncio  # Importing the asyncio module for async features
import random   # Importing the random module to generate random numbers

async def async_generator():
    """An async generator coroutine that yields 10 random numbers
    Each number is yielded after an asynchronous wait of 1 second"""
    for _ in range(10):  # Looping 10 times
        await asyncio.sleep(1)  # Asynchronously wait for 1 second
        yield random.uniform(0, 10)  # Yielding a random number between 0 and 10
