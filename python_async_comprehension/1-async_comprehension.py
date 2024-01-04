#!/usr/bin/env python3
"""Module for async_comprehension coroutine"""

import asyncio  # Importing asyncio for asynchronous features
# Importing async_generator from the previous task
from 0-async_generator import async_generator  

async def async_comprehension():
    """A coroutine that collects 10 random numbers using async comprehension
    over async_generator and returns them"""
    return [i async for i in async_generator()]  # Async Comprehension

# Rest of the code remains the same as in your 1-main.py file
