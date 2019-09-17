import sys

n, k = list(map(int, sys.stdin.readline().split()))
v = []

for _ in range(n):
    value = int(sys.stdin.readline()) 
    v.append(value)

dp = [0 for _ in range(10001)]
dp[0] = 1
for i in v:
    for j in range(i, k+1):
        dp[j] += dp[j-i]

print(dp[k])

