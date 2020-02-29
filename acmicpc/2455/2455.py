total = 0
candidate = []
for _ in range(4):
    m, n = map(int, input().split())
    total = total - m + n
    candidate.append(total)
print(max(candidate))
