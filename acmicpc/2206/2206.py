from collections import deque

N, M = map(int, input().split())
S = [list(map(int, [*input()])) for k in range(N)]
D = [[[-1]*2 for j in range(M)] for i in range(N)]
D[0][0][0] = 1
q = deque()
q.append((0, 0, 0))
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
while q:
    x, y, z = q.popleft()
    for i in range(4):
        nx, ny = x+dx[i],  y+dy[i]
        if 0<=nx<N and 0<=ny<M:
            if S[nx][ny] == 0 and D[nx][ny][z] == -1:
                D[nx][ny][z] = D[x][y][z] +1
                q.append((nx, ny, z))
            if z == 0 and S[nx][ny] == 1 and D[nx][ny][z+1] == -1:
                D[nx][ny][z+1] = D[x][y][z]+1
                q.append((nx, ny, z+1))
if D[N-1][M-1][0] == -1: print(D[N-1][M-1][1])
elif D[N-1][M-1][1] == -1: print(D[N-1][M-1][0])
else: print(min(D[N-1][M-1]))
