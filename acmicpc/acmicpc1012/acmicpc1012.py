import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    init[x][y] = True
    for dx, dy in (-1,0), (1,0), (0,1), (0,-1):
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= height or ny < 0 or ny >= width:
            continue
        if coordinate[nx][ny] and not init[nx][ny]:
            dfs(nx, ny)

def main():
    numbers = 0
    for i in range(height):
        for j in range(width):
            if coordinate[i][j] and not init[i][j]:
                dfs(i, j)
                numbers += 1
    print(numbers)


n = int(input())
for _ in range(n):
    width, height, number_of_position = map(int, input().split())
    coordinate = [[0] * width for _ in range(height)]
    init = [[False] * width for _ in range(height)]
    for _ in range(number_of_position):
        x, y = map(int, input().split())
        coordinate[y][x] = 1
    main()
