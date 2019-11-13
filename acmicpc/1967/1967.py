import collections

def f(v):
    s=m=0
    q=collections.deque()
    g = [False]*(N+1)
    g[v[0]] = True
    q.append(v)
    while q:
        v = q.popleft()
        for e in j[v[0]]:
            if not g[e[0]]:
                g[e[0]]=True
                q.append([e[0], v[1]+e[1]])
                if v[1] + e[1] > s:
                    s = v[1]+e[1]
                    m = e[0]
    return m, s

N = int(input())
j = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, w = map(int, input().split())
    j[a].append([b,w])
    j[b].append([a,w])
print(f([f([1, 0])[0], 0])[1])
