import collections
def bfs(v):
    q = collections.deque()
    q.append(v)

    while q:
        v = q.popleft()
        for a in range(8):
            i = v[0] + di[a]
            j = v[1] + dj[a]
            if 0 <= i <= h-1 and 0 <= j <= w-1 and ocean[i][j]:
                ocean[i][j] = 0
                q.append([i, j])

di = [-1, -1,-1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0, 1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    ocean = [list(map(int, input().split())) for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if ocean[i][j]:
                count += 1
                bfs([i, j])
    print(count)
