s = 'it_step_courses'
s1 = s.split('_')
s2 = s1.pop(0)
result = []
for i in s1:
    result.append(i.capitalize())
print(s2 + ''.join(result))

