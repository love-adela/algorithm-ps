import sys

n, k = list(map(int, sys.stdin.readline().split()))
coins = [int(sys.stdin.readline().strip()) for _ in range(n)]
dp = [0] + [10001]*k 

for i in coins:
    for j in range(i, k+1):
        dp[j] = min(dp[j], dp[j-i]+1)

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])
