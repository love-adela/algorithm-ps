import sys
read = lambda: sys.stdin.readline()

N = int(read())
W = [] 
for i in range(N):
    edge = [int(x) for x in read().split()]
    W.append(edge)

dp = [0] * N
dp[0][1] = 1
dp[1][0] = 1 # 양방향 연결

for i in range(1<<N):
    for j in range(N):
        if not i & (1<<j):
            continue
        current = dp[j][i]
        if current == 0:
            continue
        for k in range(N):
            if W[j][k] == 0:
                continue
            if i & (1<<k):
                continue
            distance = dp[k][i|(1<<k)]
            if distance == 0 or distance > current + W[j][k]:
                distance = current + W[j][k]

answer = float('inf')
for i in range(N):
    if dp[i][(1<<n)-1] == 0:
        continue
    if W[i][0] != 0:
        answer = min(answer, dp[i][(1<<n)-1] + W[i][0])

answer -= 1
print(answer)
