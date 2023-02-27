import asyncio
from enum import Enum


class TimeToCook(Enum):
    PASTA = 3
    SALAT = 2
    SOUP = 6


async def cook(order: str):
    time_to_cook = 0
    print(f'New order - {order}')
    if order == 'Pasta':
        time_to_cook = TimeToCook.PASTA.value
    elif order == 'Salat':
        time_to_cook = TimeToCook.SALAT.value
    elif order == 'Soup':
        time_to_cook = TimeToCook.SOUP.value
    await asyncio.sleep(time_to_cook)
    print(f'{order} Done!')


async def waiter():
    task1 = asyncio.create_task(cook("Pasta"))
    task2 = asyncio.create_task(cook("Salat"))
    task3 = asyncio.create_task(cook("Soup"))

    await task1
    await task2
    await task3

asyncio.run(waiter())



