from decorator5 import debuger
import functools


def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args):
        print("---before calling")
        func(*args)
        print("---after calling")
    return wrapper


@debuger
@my_decorator
def return_name(first_name, last_name):
    print(f"I'm {first_name} {last_name}")


return_name("John", "Connor")