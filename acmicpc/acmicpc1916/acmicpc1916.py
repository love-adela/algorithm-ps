import sys
import heapq

read = lambda: sys.stdin.readline().strip()

N = int(read())
M = int(read())

graph = [[] for _ in range(N + 1)]
visit = [False for _ in range(N + 1)]
dist = [float('inf') for _ in range(N + 1)]
heap = []

# input
for _ in range(M):
    v, u, w = map(int, read().split())
    graph[v].append([u, w])

s, e = map(int, read().split())

# dijkstra
heapq.heappush(heap, [0, s])
dist[s] = 0

while len(heap) > 0:
    while len(heap) > 0:
        _, v = heapq.heappop(heap)
        if not visit[v]:
            break
    visit[v] = True

    for nv, nw in graph[v]:
        if dist[nv] > dist[v] + nw:
            dist[nv] = dist[v] + nw
            heapq.heappush(heap, [dist[nv], nv])

# output
print(dist[e])
