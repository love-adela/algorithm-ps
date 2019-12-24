from collections import deque
N, K = map(int, input().split())

Max = 10 ** 5 
D = [-1]*(Max+1)
D[N] = 0
q = deque()
q.append(N)
while q:
    x = q.popleft()
    for nx in [x-1, x+1, 2*x]:
        if 0<=nx<=Max and D[nx]==-1:
            q.append(nx)
            D[nx] = D[x]+1

print(D[K])
