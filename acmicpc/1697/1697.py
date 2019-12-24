def bfs(v:int):
    visited = [False] * 100001
    q = [v]
    count = 0
    state = False

    while q:
        for _ in range(len(q)):
            v = q.pop(0)
            if not visited[v]:
                visited[v] = True
                if v == M:
                    state = True
                    break
                if v - 1 >= 0 :
                    q.append(v-1)
                if v + 1 <= 1000000:
                    q.append(v+1)
                if v * 2 <= 1000000:
                    q.append(v*2)
        if state:
            return count
        count += 1

N, M = map(int, input().split())
print(bfs(N))
