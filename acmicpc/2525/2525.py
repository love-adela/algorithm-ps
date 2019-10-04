h, m = map(int, input().split())
duration = int(input())
m += duration
exc_m = m // 60
if exc_m >= 1:
    h += exc_m
    m -= 60 * exc_m

exc_h = h // 24
if exc_h >= 1:
    h -= 24 * exc_h
print(h, m)
