import sys
from collections import deque

A, B, N, M = map(int, sys.stdin.readline().split())
max_num = 100001
visited = [False] * max_num

case = N

def bfs(start, distance):
    q = deque()
    q.append([start, distance])
    visited[start] = True
    while q:
        x, d = q.popleft()
        case = [x+1, x-1, x+A, x-A, x+B, x-B, x*A, x*B]
        if x == M:
            return d
        for x in case:
            if x > 100000 or x < 0 or visited[x]:
                continue
            else:
                q.append([x, d+1])
                visited[x] = True

print(bfs(N, 0))
