from threading import Timer
import os


def timer():
    timer_ = Timer(interval=5.0, function=func)
    timer_.start()


def func():
    for i in os.listdir():
        print(i)
    timer()


func()