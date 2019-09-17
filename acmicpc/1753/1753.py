import sys 
import heapq

read = lambda: sys.stdin.readline().strip()

V, E = map(int, read().split())
K = int(read())
INF = 987654321

a = [ [] for _ in range(V+1)]
d = [INF] * (V+1)

for _ in range(E):
    u, v, w = map(int, read().split())
    a[u].append((v, w))

# dijkstra
def sol(start):
    pq = []
    d[start] = 0
    heapq.heappush(pq, (d[start], start))

    while pq:
        dist, here = heapq.heappop(pq)
        if d[here] < dist:
            continue
        for there, _w in a[here]:
            if d[there] > dist + _w:
                d[there] = dist + _w
                heapq.heappush(pq, (d[there], there))

sol(K)
for num in d[1:]:
    print('INF') if num == INF else print(f'{num}') 

