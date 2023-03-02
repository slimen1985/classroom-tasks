import math
import multiprocessing as mp
import random


def get_cubs(num: int):
    for _ in range(num):
        yield [math.pow(random.randint(1, 10), 3) for _ in range(3)]


if __name__ == "__main__":
    queue = mp.Queue()
    cubes = iter(get_cubs(3))
    queue.put(next(cubes))
    queue.put(next(cubes))
    queue.put(next(cubes))

    while not queue.empty():
        print(queue.get())








