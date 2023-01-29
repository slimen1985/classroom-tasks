import random


class MyIterator:
    def __init__(self, n, start, end ):
        self.n = n
        self.start = start
        self.end = end
        self.count = 0

    def __next__(self):
        res = random.randint(self.start, self.end)
        if self.count < self.n:
            self.count +=1
            return res
        raise StopIteration

    def __iter__(self):
        return self


l = MyIterator(3, 10, 20)
for i in l:
    print(i, end=" ")


