import sys
read = lambda: sys.stdin.readline()
T = int(read())
K = [] # (3 <= K <= 500)
sizes = [] # 10000이하

for t in range(T):
    K.append(int(read()))
    sizes.append(list(map(int, read().split())))

for t in range(T):
    k = K[t]
    s = sizes[t]

    total = [s[0]]
    for i in s[1:]:
        total.append(i+total[-1])
    dp = [[0] * k for _ in range(k)]
    dp[0][1] = total[1]
    for i in range(1, k-1):
        dp[i][i+1] = total[i+1]-total[i-1]

    for gap in range(2, k):
        for i in range(k-gap):
            dp[i][i+gap] = float('inf')
            for j in range(i, i+gap):
                dp[i][i+gap] = min(dp[i][i+gap], dp[i][j]+dp[j+1][i+gap])
            dp[i][i+gap] = dp[i][i+gap] + total[i+gap]-total[i-1] if i > 0 else dp[0][gap]+total[gap]

    print(dp[0][k-1])
