inf = 10000000000
result = inf

n = int(input())
togo = 0
rest = 0

for i in range(n):
    togo, rest = map(int, input().split())
    if togo <= rest:
        result = min(result, rest)
if result == inf:
    print(-1)
else:
    print(result)
