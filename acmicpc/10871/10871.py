x, n = map(int, input().split())
a = list(map(int, input().split()))

for i in range(x):
    if n > a[i]:
        print(a[i], end=' ')
