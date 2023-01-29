def double_it(func):
    def wrapper(*args):
        val = func(*args)
        return val * 2
    return wrapper


@double_it
def multiply(num1, num2):
    return num1 * num2


@double_it
def get_sum(*args):
    return sum(args)


print(multiply(5, 4))
print(get_sum(2, 5, 3, 4, 5))