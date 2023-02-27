import asyncio


async def func1(num: int) -> None:
    await asyncio.sleep(2)
    return num ** 2


async def func2(num: int) -> None:
    await asyncio.sleep(3)
    return num ** 3


async def main():
    result = await asyncio.gather(
        func1(2),
        func2(3)
    )

    print(result)


asyncio.run(main())
