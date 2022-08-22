a, b = map(int, input().split())

defense = 0
defense = a - a * b * 0.01


if defense >= 100:
    print(0)
else:
    print(1)
