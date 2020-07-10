N = int(input())
grid = [[0] * 100 for _ in range(101)]
area = 0
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(y, y+10):
        for j in range(x, x+10):
            grid[i][j] = 1

for coor in grid:
    for elem in coor:
        if elem:
            area += 1
print(area)
