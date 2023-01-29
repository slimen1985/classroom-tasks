import sys


def fact(i):
    return 1 if i == 1 else i * fact(i - 1)


if __name__ == "__main__":
    print(sys.argv[0])
    if len(sys.argv) > 1:
        print(fact(int(sys.argv[1])))
