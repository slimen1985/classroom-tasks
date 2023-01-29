def debuger(func):
    def wrapper(*args, **kwargs):
        arg_list = [str(i) for i in args]
        kwarg_list = [f"{key}={value}" for key, value in kwargs.items()]
        subscription = ", ".join(arg_list + kwarg_list)
        print(f"Calling {func.__name__} with parameters {subscription}")
        val = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {val}")
        return val
    return wrapper

# @debuger
# def get_GCD(a, b):
#     if b == 0:
#         return a
#     else:
#         return get_GCD(b, a % b)
#
#
# print(get_GCD(45, 30))
