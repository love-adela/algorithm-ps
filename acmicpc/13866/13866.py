levels = sorted([int(param) for param in input().split()])
m = levels[1] - levels[0]
n = levels[3] - levels[2]

if m <= n:
    print(n-m)
else:
    print(m-n)
