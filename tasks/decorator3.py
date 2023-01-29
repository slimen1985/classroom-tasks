def my_decorator(func):
    def wrapper(*args):
        print("---before calling")
        func(*args)
        print("---after calling")
    return wrapper


def return_name(first_name, last_name):
    print(f"I'm {first_name} {last_name}")


f = my_decorator(return_name)
f("John", "Connor")