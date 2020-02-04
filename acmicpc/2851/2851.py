total = 0
for _ in range(10):
    grade = int(input())
    a = total
    total += grade
    if total >= 100:
        break

if abs(100-a) == abs(100-total):
    if a > total:
        print(a)
    else:
        print(total)
else:
    if abs(100-a) > abs(100-total):
        print(total)
    else:
        print(a)

