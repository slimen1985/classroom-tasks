from collections.abc import Iterable, Iterator

l = [1, 2, 3]
li = iter(l)

# print(isinstance(li, Iterable))
# print(isinstance(li, Iterator))
# print(dir(li))
# print(next(li))
# print(next(li))
# print(next(li))
# print(next(li))
print(type(l))
print(type(li))

for i in li:
    print(i)