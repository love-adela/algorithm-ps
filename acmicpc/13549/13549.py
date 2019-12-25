from collections import deque
N, K = map(int, input().split())
Max = 10**5+1
D = [-1]*Max
D[N] = 0
q = deque([N])
while q:
    x = q.popleft()
    for nx in [2*x, x+1, x-1]:
        if 0<=nx<Max and D[nx] == -1:
            if nx == 2*x:
                q.appendleft(nx)
                D[nx] = D[x]
            else:
                q.append(nx)
                D[nx] = D[x]+1
print(D[K])
