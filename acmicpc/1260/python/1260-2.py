import sys

read = lambda: sys.stdin.readline()
N, M, V = map(int, read().split())

graph = dict()
for _ in range(M):
    u, v = map(int, read().split())
    if u in graph:
        graph[u].append(v)
    else: graph[u] = [v]
    if v in graph:
        graph[v].append(u)
    else:
        graph[v] = [u]

for _, edges in graph.items():
    edges.sort(reverse=True)

def dfs(graph, start):
    visited = {x: False for x in graph}
    candidates = [start]
    result = []
    while candidates:
        curr = candidates.pop()
        if visited[curr]: continue
        visited[curr] = True
        result.append(curr)
        for node in graph[curr]:
            candidates.append(node)
    return result 

answer = dfs(graph, V)
print(' '.join([str(param) for param in answer]))
                
                
for _, edges in graph.items():
    edges.sort()

def bfs(graph, start):
    visited = {x: False for x in graph}
    candidates = [start]
    result = []

    while candidates:
        curr, *candidates = candidates
        if visited[curr]: continue
        visited[curr] = True
        result.append(curr)
        for node in graph[curr]:
            candidates.append(node)
    return result

res = bfs(graph, V)
print(' '.join([str(param) for param in res]))

