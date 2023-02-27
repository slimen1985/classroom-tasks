import time


def func1(num: int) -> None:
    print(num ** 2)
    time.sleep(2)


def func2(num: int) -> None:
    print(num ** 3)
    time.sleep(3)


def main():
    func1(5)
    func2(10)


if __name__ == "__main__":
    main()
    print('End')