a, b = int(input()), int(input())
result = 0
while a >= b:
    a -= b
    result += 1
print(a, result)
