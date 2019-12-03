import sys
sys.setrecursionlimit(10000)

def dsf(i:int, G:list, V:list, N:int):
    V[i] = True
    for j in range(1, N+1):
        if V[j] == True or G[i][j] == 0:
            continue
        dsf(j, G, V, N)

def main():
    adj = [[0]*1001 for _ in range(1001)]
    visited = [0]*1001

    N, M = map(int, input().split())
    for i in range(M):
        u, v = map(int, sys.stdin.readline().split())
        adj[u][v] = 1
        adj[v][u] = 1
    count = 0

    for i in range(1, N+1):
        if visited[i] == 0:
            dsf(i, adj, visited, N)
            count += 1

    print(count)
main()
