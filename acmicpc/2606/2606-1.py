C = int(input()) # 정점의 개수
N = int(input()) # 간선의 개수
G = [[False for _ in range(C+1)] for _ in range(C+1)]

for _ in range(N):
    a, b = map(int, input().split())
    G[a][b] = True
    G[b][a] = True

def dfs(graph, start):
    candidates = [start]
    visited = [False] * (len(graph)+1)

    while candidates:
        u = candidates.pop()
        for v in range(len(graph)):
            if graph[u][v] and not visited[v]:
                visited[v] = True
                candidates.append(v)
    return visited

res = dfs(G, 1)
print(sum(res) -1)
