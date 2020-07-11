import sys
input = sys.stdin.readline
N, M = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

direction = [[-1, 0], [0, -1], [1, 0], [0, 1]]
maximum = -1

def get_grid(x, y):
    global maximum
    elem = grid[x][y]
    if (x == 0) and (y == 0 or y == M-1): return
    if (x == N-1) and (y == 0 or y == M-1): return

    if x == 0:
        elem += grid[x+1][y] + grid[x][y-1] + grid[x][y+1]
    elif x == N-1:
        elem += grid[x-1][y] + grid[x][y-1] + grid[x][y+1]
    elif y == 0:
        elem += grid[x][y+1] + grid[x-1][y] + grid[x+1][y]
    elif y == M-1:
        elem += grid[x][y-1] + grid[x-1][y] + grid[x+1][y]
    else:
        temp = []
        temp.append(grid[x+1][y] + grid[x][y-1] + grid[x][y+1])
        temp.append(grid[x-1][y] + grid[x][y-1] + grid[x][y+1])
        temp.append(grid[x][y+1] + grid[x-1][y] + grid[x+1][y])
        temp.append(grid[x][y-1] + grid[x-1][y] + grid[x+1][y])
        elem += max(temp)
    maximum = max(maximum, elem)

def dfs(x, y, count, total):
    global maximum
    if count == 4:
        maximum = max(maximum, total)
        return 
    for d in direction:
        new_x = x + d[0]
        new_y = y + d[1]
        if 0 <= new_x < N and 0 <= new_y < M and not visited[new_x][new_y]:
            if grid[new_x][new_y] == -1:
                continue
            visited[new_x][new_y] = True
            dfs(new_x, new_y, count+1, total+grid[new_x][new_y])
            visited[new_x][new_y] = False

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 1, grid[i][j])
        get_grid(i, j)
        visited[i][j] = False

print(maximum)

