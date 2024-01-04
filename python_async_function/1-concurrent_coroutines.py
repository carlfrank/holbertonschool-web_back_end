#!/usr/bin/env python3
"""execute multiple coroutines at the same
time with async"""
import asyncio
from typing import List
from importlib import import_module

# Importing the module dynamically
module_name = '0-basic_async_syntax'
module = import_module(module_name)
wait_random = module.wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """execute multiple coroutines at the same
    time with async"""
    tasks = (wait_random(max_delay) for _ in range(n))
    lst = await asyncio.gather(*tasks)
    return sorted(lst)
