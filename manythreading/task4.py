from threading import Thread, Event
from time import sleep


event = Event()


def worker(name: str):
    event.wait()  # блокируемся, пока событие не будет установлено
    print(name)


# Создаем поток и передаем ему событие
threads = [Thread(target=worker, args=(f'worker {i} ',)) for i in range(4)]

for thread in threads:
    thread.start()

print("Main thread")

event.set()
