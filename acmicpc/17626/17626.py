n = int(input())

fs = [i*i for i in range(224)]
dp = [4 for x in range(n+1)]
visit = [0 for x in range(n+1)]
dp[0] = 0
dp[1] = 1

exNum = 50000**2
for i in range(1, n+1):
    minNum = exNum
    j = 1
    while(not visit[i] and fs[j] <= i):
        minNum = min(dp[i-fs[j]], minNum)
        j = j+1
    visit[i] = 1
    dp[i] = minNum+1

print(dp[n])

