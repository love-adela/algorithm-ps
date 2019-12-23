def dfs(now:int, graph:list, visited:list)->list:
    visited += [now]

    for i in range(len(graph[now])):
        if graph[now][i] and i not in visited:
            visited = dfs(i, graph, visited)
    return visited


def bfs(start:int)->list:
    queue = [start]
    visited = [start]
    while queue:
        current = queue.pop(0)
        for i in range(len(matrix[current])):
            if matrix[current][i] and i not in visited:
                visited += [i]
                queue += [i]
    return visited


n, m, v = map(int, input().split())
matrix = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    matrix[x][y] = 1
    matrix[y][x] = 1

print(*dfs(v, matrix, []))
print(*bfs(v))
