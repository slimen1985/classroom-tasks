import time


def timer(func):
    def wrapper(i):
        start = time.time()
        val = func(i)
        end = time.time() - start
        print(f"execution time for {func.__name__} is {end} sec")
        return val
    return wrapper


@timer
def get_factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * get_factorial(num - 1)


print(get_factorial(5))
