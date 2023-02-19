from multiprocessing import Process
import os


def get_double_value(num: int):
    res = num * 2
    proc_id = os.getpid()
    print(f'{num} doubled to {res} by {proc_id}')


if __name__ == "__main__":
    numbers = [i for i in range(10)]
    process = []

    for index, value in enumerate(numbers):
        proc = Process(target=get_double_value, args=(value, ))
        process.append(proc)
        proc.start()

    for pr in process:
        pr.join()
