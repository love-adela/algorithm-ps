m, n = map(int, input().split())
if m + n < 0 or m - n < 0 or (m+n) % 2:
    print(-1)
else:
    a = (m+n) // 2
    b = m-a
    print(max(a, b), min(a, b))
