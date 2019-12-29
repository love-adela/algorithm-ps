from collections import deque
r,c=map(int,input().split())
S=[input() for _ in range(r)]
dx,dy=[0,0,1,-1],[1,-1,0,0]
water_D=[[-1]*c for _ in range(r)]
D=[[-1]*c for _ in range(r)]
q=deque()
for i in range(r):
    for j in range(c):
        if S[i][j]=='*':
            q.append((i,j))
            water_D[i][j]=0
        elif S[i][j]=='S':
            sx,sy=i,j
        elif S[i][j]=='D':
            ex,ey=i,j
while q:
    x,y=q.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<r and 0<=ny<c and S[nx][ny] not in 'DX' and water_D[nx][ny]==-1:
            water_D[nx][ny]=water_D[x][y]+1
            q.append((nx,ny))
q.append((sx,sy))
D[sx][sy]=0
while q:
    x,y=q.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<r and 0<=ny<c and D[nx][ny]==-1 and S[nx][ny] not in '*X':
            if water_D[nx][ny]==-1 or D[x][y]+1<water_D[nx][ny]:
                D[nx][ny]=D[x][y]+1
                q.append((nx,ny))
print([D[ex][ey],'KAKTUS'][D[ex][ey]==-1])
