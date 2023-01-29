def concat(a, b):
    return "{} {}".format(a, b)


def sum_numbers(a, b, c):
    return a + b + c


def multiply_numbers(a, b, c):
    return a * b * c


def test_concat():
    assert concat(2, 1) == "2 1"
    assert concat("a", "b") == "a, b"


def test_sum_numbers():
    assert sum_numbers(1, 2, 3) == 6


def test_multiply_numbers():
    assert multiply_numbers(1, 2, 3) == 6
    assert multiply_numbers(2, 2, 3) == 12


test_functions = [
    test_concat,
    test_sum_numbers,
    test_multiply_numbers
]

if __name__ == "__main__":
    for func in test_functions:
        try:
            func()
        except Exception as err:
            print(f"Failed -> {func.__name__}, {type(err)}, {err}")