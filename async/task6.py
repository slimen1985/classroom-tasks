import random
import asyncio
import math


async def generate_cube(num=3):
    await asyncio.sleep(1)
    print([math.pow(random.randint(1, 10), 3) for _ in range(num)])


async def main():
   tasks = [asyncio.create_task(generate_cube(), name=f'worker#{i}') for i in range(5)]
   for task in tasks:
       await task

asyncio.run(main())
