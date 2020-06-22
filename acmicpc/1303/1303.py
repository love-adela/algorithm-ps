import sys
read = lambda : sys.stdin.readline()
N, M = map(int, read().split())
coordinates = [[*read()] for i in[0]*M]
visited = [[False] * N for _ in range(M)]
white, black = 0, 0

def dfs(x, y, item):
    candidates = [(x, y)]
    visited[x][y] = True
    cnt = 1 
    while candidates:
        curr = candidates.pop()
        for delta_x, delta_y in (-1, 0), (1, 0), (0, -1), (0, 1):
            new_x, new_y = curr[0]+delta_x, curr[1]+delta_y
            if 0 <=new_x<M and 0<= new_y < N:
                if not visited[new_x][new_y] and coordinates[new_x][new_y] == item:
                    visited[new_x][new_y] = True
                    candidates.append((new_x, new_y))
                    cnt += 1
    return cnt

for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            res = dfs(i, j, coordinates[i][j])
            if coordinates[i][j] == 'W': white += res**2
            else: black+= res**2

print(white, black)
