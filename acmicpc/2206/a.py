from collections import deque
n,m=map(int,input().split())
S=[list(map(int,[*input()])) for k in range(n)]
D= [[[-1]*2 for j in range(m)] for i in range(n)]
D[0][0][0]=1
q=deque()
q.append((0,0,0))
dx,dy=[0,0,1,-1],[1,-1,0,0]
while q:
    x,y,z=q.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if S[nx][ny]==0 and D[nx][ny][z]==-1:
                D[nx][ny][z]=D[x][y][z]+1
                q.append((nx,ny,z))
            if z==0 and S[nx][ny]==1 and D[nx][ny][z+1]==-1:
                D[nx][ny][z+1]=D[x][y][z]+1
                q.append((nx,ny,z+1))
if D[n-1][m-1][0]==-1:print(D[n-1][m-1][1])
elif D[n-1][m-1][1]==-1:print(D[n-1][m-1][0])
else:print(min(D[n-1][m-1]))
