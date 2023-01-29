from custom_exceptions import WrongTypeOfArgument


def check_numbers(num: int) -> bool:
    if not isinstance(num, int):
        raise WrongTypeOfArgument
    return num % 2 == 0


print(check_numbers(6))