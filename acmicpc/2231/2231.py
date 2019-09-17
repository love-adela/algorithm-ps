N = int(input())
ans = []

for i in range(N-1, 0, -1):
    d = [int(d) for d in str(i)]
    if N == i + sum(d):
        ans.append(i)

if len(ans) > 0:
    print(min(ans))
else:
    print(0)

