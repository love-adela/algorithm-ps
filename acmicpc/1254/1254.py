#! usr/bin/python
import sys

read = lambda: sys.stdin.readline().strip()
S = read()
dp = [[0 for _ in range(len(S))] for _ in range(len(S))]
for i in range(len(S)-1,-1,-1):
    for j in range(i,len(S)):
        if i == j: 
            dp[i][j] = 1
        elif j-1 == i and S[i] == S[j]: 
            dp[i][j] = 1
        elif dp[i+1][j-1]== 1 and S[i] == S[j]: 
            dp[i][j] = 1

index = 0
for i in range(len(S)):
    if dp[i][len(S)-1] == 1:
        index = i
        break
print(len(S) + index)
