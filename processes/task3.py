from multiprocessing import Process, Pipe
from multiprocessing.dummy.connection import Connection
from typing import List


def func(connection: Connection, lst: List[int]):
    print("Sending object ...")
    connection.send(lst)
    connection.close()


if __name__ == '__main__':
    lst_ = [i for i in range(10)]
    parent, child = Pipe()
    proc = Process(target=func, args=(child, lst_, ))
    proc.start()
    print(parent.recv())
    proc.join()

