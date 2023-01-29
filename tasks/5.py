a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a == b == c != d:
    print(d)
elif b == c == d != a:
    print(a)
elif a == b == d != c:
    print(c)
else:
    print(a)
