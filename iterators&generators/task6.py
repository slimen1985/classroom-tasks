from collections.abc import Iterator, Iterable
import math


class MyIterator:
    def __init__(self):
        self.num = 1

    def __next__(self):
        result = self.num**2
        if self.num > 10:
            raise StopIteration("No more ")
        self.num += 1
        return result


class MyIterable:
    def __iter__(self):
        return MyIterator()


l = MyIterable()

for i in l:
    print(i)









