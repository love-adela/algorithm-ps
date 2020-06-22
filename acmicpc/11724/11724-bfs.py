import sys
from collections import deque

sys.setrecursionlimit(10000)

def bfs(i:int, neighbor:list, visited:list, node:int):
    visited[i] = True
    d = deque()
    d.append(node)
    while d:
        a = d.popleft()
        for elem in neighbor[a]:
            if not visited[elem]:
                d.append(elem)
                visited[elem] = True

def main():
    adj = [[0]*10001 for _ in range(1001)]
    visited = [0]*1001

    N, M = map(int, input().split())
    for i in range(M):
        u, v = map(int, sys.stdin.readline().split())
        adj[u][v] = 1
        adj[v][u] = 1
    count = 0

    for i in range(1, N+1):
        if visited[i] == 0:
            bfs(i, adj, visited, N)
            count += 1
    print(count)
main()
