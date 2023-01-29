import sys

try:
    f = open('test.txt')
    s = f.readline()
    i = s.split()
    from math import s
except FileNotFoundError as err_:
    print(f"No such file {err_}")
    # raise err_
except ImportError as err:
    print(f"Import error {err}")

print("Hi")