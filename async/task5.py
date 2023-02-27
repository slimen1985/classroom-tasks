import asyncio


async def worker(number: int, divider: int):
    print(f'Worker started with {number}')
    await asyncio.sleep(3)
    return number/divider


async def worker_gather():
    res = await asyncio.gather(
        worker(50, 10),
        worker(60, 6),
        worker(30, 3)
    )

    print(res)


event_loop = asyncio.get_event_loop()
task_list = [
    event_loop.create_task(worker_gather())
]
tasks = asyncio.wait(task_list)
event_loop.run_until_complete(tasks)
event_loop.close()