result = []
total = 0
for _ in range(10):
    a, b = map(int, input().split())
    total = total + b - a
    result.append(total)
print(max(result))
