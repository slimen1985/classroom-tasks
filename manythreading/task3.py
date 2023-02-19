import random
from threading import Thread, Semaphore
from time import sleep


def get_random(semaphore: Semaphore, number: int):
    with semaphore:
        print(f'Num of threads {semaphore._value}')
        value = random.random()
        sleep(1)
        print(f'Thread #{number} produced {value}')


semaphore = Semaphore(5)

for i in range(9):
    worker = Thread(target=get_random, args=(semaphore, i))
    worker.start()

