import asyncio


async def func1(num: int) -> None:
    print(num ** 2)
    await asyncio.sleep(2)
    print(f'End {func1.__name__}')


async def func2(num: int) -> None:
    print(num ** 3)
    await asyncio.sleep(3)
    print(f'End {func2.__name__}')


async def main():
    task1 = asyncio.create_task(func1(4), name="Task1")
    task2 = asyncio.create_task(func2(8), name="Task2")

    await task1
    await task2


asyncio.run(main())