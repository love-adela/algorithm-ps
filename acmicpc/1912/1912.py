import sys

read = lambda: sys.stdin.readline()

n = int(read())
lst = [0] + list(map(int, input().split()))
dp = [0] * (n+1)
answer = dp[1] = lst[1]

for i in range(2, n+1):
    dp[i] = max([lst[i], dp[i-1]+lst[i]])
    answer = max([answer, dp[i]])
print(answer)
