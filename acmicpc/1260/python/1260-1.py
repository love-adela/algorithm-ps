import sys
from collections import deque
read = lambda: sys.stdin.readline()
N, M, V = map(int, read().split())
# 정점의 개수 : N
# 간선의 개수 : M
# 탐색 시작할 정점 번호 : V

neighbor = [[] for _ in range(N+1)] 
for i in range(M):
    a, b = map(int, read().split())
    neighbor[a].append(b)
    neighbor[b].append(a)

neighbor = [sorted(param) for param in neighbor]
print(neighbor)
visited = [False]*(N+1)

def dfs(n):
    visited[n] = True
    print(n, end=' ')
    for elem in neighbor[n]:
        if not visited[elem]:
            dfs(elem)

def bfs(n):
    visited[n] = True
    d = deque()
    d.append(n)
    while d:
        a = d.popleft()
        print(a, end=' ')
        for elem in neighbor[a]:
            if not visited[elem]:
                d.append(elem)
                visited[elem] = True


dfs(V)
print()
visited = [False]*(N+1)
bfs(V)
