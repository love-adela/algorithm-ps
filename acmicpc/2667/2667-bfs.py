import sys
read = lambda: sys.stdin.readline().strip()

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(matrix, x, y, count):
    matrix[x][y] = 0
    queue = []
    queue.append((x, y))
    while len(queue) > 0:
        x, y = queue.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx and nx < n and 0 <= ny and ny < n:
                if matrix[nx][ny] == 1:
                    count += 1
                    matrix[nx][ny] = 0
                    queue.append((nx, ny))
    return count

count = 0 
n = int(read())
matrix = [list(map(int, list(read()))) for _ in range(n)]

ans = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            ans.append(bfs(matrix, i, j, count +1))

print(len(ans))
for i in sorted(ans):
    print(i)
