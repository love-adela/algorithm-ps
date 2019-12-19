from itertools import combinations
def euclidean(m, n):
    if n == 0:
        return m
    if m%n == 0:
        return n
    return euclidean(n, m%n)

n = int(input())
for _ in range(n):
    n, *params  = map(int, input().split())
    combs=list(combinations(params, 2))
    a = [euclidean(params[0], params[1]) for params in combs]
    print(sum(a))
