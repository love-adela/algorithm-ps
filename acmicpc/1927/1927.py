import sys
import heapq

read = lambda: sys.stdin.readline().strip()

N = int(read())

heap = []

for _ in range(N):
    x = int(read())
    if x == 0:
        if len(heap) > 0:
            print(heapq.heappop(heap))
        else:
            print(0)

    else:
        heapq.heappush(heap, x)
