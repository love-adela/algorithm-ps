t = [int(input()) for _ in range(4)]
h = sum(t) // 60
print(h)
m = sum(t) - 60 * h
print(m)
