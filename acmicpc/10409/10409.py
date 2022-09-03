n, T = map(int, input().split())
minutes = [int(param) for param in input().split()]
total, count = 0, 0

for item in minutes:
    total += item
    if total > T:
        break
    count += 1

print(count)
