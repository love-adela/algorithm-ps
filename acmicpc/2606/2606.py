C = int(input()) # 컴퓨터의 수
N = int(input()) # 네트워크의 수
neighbor = [[0 for _ in range(C+1)] for _ in range(C+1)]

for _ in range(N):
    m, n = map(int, input().split())
    neighbor[m][n] = 1
    neighbor[n][m] = 1

def bfs(lst, start):
    queue = [start]
    visited = []
    while queue:
        a = queue.pop(0)
        visited.append(a)
        for i in range(len(lst)):
            if lst[a][i] and i not in visited and i not in queue:
                queue.append(i)

    return len(visited)


print(bfs(neighbor, 1)-1)
