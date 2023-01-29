def say_hello(name):
    print(f"Hello {name}")


def say_by(name):
    print(f"Goodbye {name}")


def greeter(func):
    return func("Mike")


greeter(say_hello)