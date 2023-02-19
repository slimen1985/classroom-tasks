from threading import Thread, Semaphore
from time import sleep

semaphore = Semaphore(4)


def show_name(name: str):
    with semaphore:
        print(semaphore._value)
        for i in range(6):
            print(name, end='\n')
            sleep(1)
        print('End sequence')


threads = [Thread(target=show_name, args=(f'thread #{i}',)) for i in range(6)]

for thread in threads:
    thread.start()


for thread in threads:
    thread.join()