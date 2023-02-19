from threading import Thread, Event
import time
import random

event = Event()


def producer():
    print('Product found')
    time.sleep(2)
    event.set()
    event.clear()


def consumer():
    print("Product wait")
    event.wait()
    print("Event exit")


# Создаем потоки для выполнения функций
worker1= Thread(target=producer)
worker2 = Thread(target=consumer)

# Запускаем потоки
worker2.start()
worker1.start()

# Ждем, пока потоки завершат работу
worker1.join()
worker2.join()

print("done")


