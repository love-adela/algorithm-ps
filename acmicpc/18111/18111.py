import sys
read = lambda: sys.stdin.readline()
N, M, B = map(int, read().split())

grid = []
height = 256
(max_res, min_res) = (sys.maxsize, 0)

for i in range(N):
    grid.append(list(map(int, input().split())))
    height = min(height, min(grid[i]))

for k in range(height, 257):
    cost, inventory = 0, B

    for i in range(N):
        for j in range(M):
            if grid[i][j] > k:
                cost += (2*(grid[i][j] - k))
                inventory += (grid[i][j] - k)
            else:
                cost += k - grid[i][j]
                inventory -= k - grid[i][j]
    if inventory < 0: 
        break
    else:
        if cost < max_res: 
            (max_res, min_res) = (cost, k)
        elif cost == max_res:
            min_res = k
print(max_res, min_res)
