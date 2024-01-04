#!/usr/bin/env python3
"""Module for measure_runtime coroutine"""

import asyncio
import time
from 1-async_comprehension import async_comprehension  # Import async_comprehension from the previous task

async def measure_runtime():
    """Measure the runtime of executing async_comprehension four times in parallel"""
    start_time = time.time()  # Record the start time
    await asyncio.gather(*(async_comprehension() for _ in range(4)))  # Run four async_comprehensions concurrently
    end_time = time.time()  # Record the end time
    return end_time - start_time  # Return the total runtime

# The rest of the code, which calls and prints the measure_runtime coroutine's result.
async def main():
    return await(measure_runtime())

print(
    asyncio.run(main())
)
