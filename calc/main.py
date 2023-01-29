from operations import *
import sys


def runner():
        if len(sys.argv) == 4:
            a = int(sys.argv[1])
            b = int(sys.argv[2])
            op = sys.argv[3]
            if op == "+":
                print(get_sum(a, b))
            elif op == "-":
                print(get_sub(a, b))
            elif op == "/":
                print(get_div(a, b))
            elif op == "*":
                print(get_mult(a, b))
        else:
            print("Three args are needed")

if __name__ == "__main__":
    runner()