def my_decorator(func):
    num = 2
    def wrapper():
        nonlocal num
        func() if num == 1 else print("wrong number")
    return wrapper


def return_name():
    print("I'm Groot!")


f = my_decorator(return_name)
f()