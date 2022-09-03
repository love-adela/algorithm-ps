t = int(input())
for _ in range(t):
    n = int(input())
    d = 0
    while (d+1) + (d+1)**2 <= n:
        d += 1
    print(d)
