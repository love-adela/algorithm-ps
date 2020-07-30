N, M = map(int, input().split())
unknown_not_listened = {input() for param in range(N)}
unknown_not_seen = {input() for param in range(M)}

intersection = sorted(unknown_not_listened & unknown_not_seen)
print(len(intersection))
for item in intersection:
    print(item)
