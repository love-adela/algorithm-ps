y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())
age = 0

if m1 < m2:
    age = y2 - y1
elif m1 == m2:
    if d1 <= d2:
        age = y2 - y1
    else:
        age = y2 - y1 -1
else:
    age = y2 - y1 - 1
print(age)
print(y2 - y1 + 1)
print(y2 - y1)
