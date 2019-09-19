import sys
from itertools import accumulate
input = sys.stdin.readline

n, m = map(int, input().split())
f = lambda x: 1 if x == 'W' else 0
b = [[0 for _ in range(m+1)]]
for i in range(n):
    cost = [0]
    cost.extend(accumulate([(f(s)+i+j) % 2 for j, s in enumerate(input().rstrip())]))
    b.append([k+j for k, j in zip(cost, b[-1])])

result = 32
for i in range(8, n+1):
    for j in range(8, m+1):
        x = b[i][j] + b[i-8][j-8] - b[i][j-8] - b[i-8][j]
        result = min(result, x, 64-x)
print(result)
