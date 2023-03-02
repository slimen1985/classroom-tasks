import multiprocessing as mp


def cube(num: int) -> int:
    return num**3


if __name__ == '__main__':
    pool = mp.Pool(processes=3)
    process = [pool.apply_async(cube, args=(num,)) for num in range(1, 1000)]
    res = [proces.get() for proces in process]
    print(res)