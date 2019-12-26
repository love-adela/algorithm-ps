import sys
from collections import deque
 
n = int(sys.stdin.readline())
d = [[-1]*1001 for _ in range(1001)]
d[1][0] = 0  # 화면 1개, 클립보드 0개
q = deque()
q.append((1,0))
 
while q:
    s, c = q.popleft()
 
    if d[s][s] == -1:
        d[s][s] = d[s][c] + 1
        q.append((s, s))
    if s+c<=n and d[s+c][c] == -1:
        d[s+c][c] = d[s][c] + 1
        q.append((s+c,c))
    if s-1>=0 and d[s-1][c] == -1:
        d[s-1][c] = d[s][c] + 1
        q.append((s-1,c))
ans = -1
for i in range(n):
    if d[n][i] != -1:
        if ans == -1 or ans > d[n][i]:
            ans = d[n][i]
print(ans)

