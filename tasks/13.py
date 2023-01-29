from typing import Tuple
def get_digits(nums: str) -> tuple[int]:
        return tuple(map(int, nums))

nums = input()
print(get_digits(nums))