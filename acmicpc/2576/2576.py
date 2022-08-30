odds = []
for _ in range(7):
    param = int(input())
    if param % 2 == 1:
        odds.append(param)

if odds:
    print(sum(odds))
    print(min(odds))
else:
    print(-1)
