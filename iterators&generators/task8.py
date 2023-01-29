import random


def num_generator(n, start, end):
    while n > 0:
        yield random.randint(start, end)
        n -= 1


g = num_generator(3, 10, 20)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
