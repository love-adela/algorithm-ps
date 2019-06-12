score = []
for _ in range(8):
    score.append(int(input()))

largest = sorted(score, reverse=True)[:5]
print(sum(largest))

index = []
for i in largest:
    index.append(str(score.index(i) + 1))

print(' '.join(sorted(index)))
