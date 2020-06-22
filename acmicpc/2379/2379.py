T = int(input())

def dfs(graph, start):
    candidates = [start]
    visited = [False] * (len(graph)+1)

    while candidates:
        curr = candidates.pop()
        for node in graph[curr]:
            if not visited[node]:
                visited[node] = True
                candidates.append(node)
    return visited

for _ in range(T):
    G = int(input())
    dfs()
