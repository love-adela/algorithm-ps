import sys

def bfs(vertex:int, distance:int):
    queue = [vertex]
    visited = [False] * N
    flag = False

    while queue:
        vertex = queue.pop(0)
        if not visited[vertex]:
            visited[vertex] = True
            for elem in adjacent[vertex]:
                if elem == distance:
                    print(1, end=" ")
                    flag = True
                    break
                if not visited[elem]:
                    queue.append(elem)
            if flag:
                break
    else:
        print(0, end=" ")

N = int(input())
adjacent = [[]for _ in range(N)]

for i in range(N):
    matrix = list(map(int, sys.stdin.readline().split()))
    for j in range(len(matrix)):
        if matrix[j]:
            adjacent[i].append(j)

for i in range(N):
    for j in range(N):
        bfs(i, j)
    print()
