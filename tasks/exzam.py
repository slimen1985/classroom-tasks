grades = input().split()
a_count = 0
for grade in grades:
    if grade == 'A':
        a_count += 1

print(round(a_count / len(grades), 2))