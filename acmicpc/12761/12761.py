import sys
max_num = 100001
visited = [False] * max_num 
queue = []
A, B, N, M = map(int, sys.stdin.readline().split())

queue.append((N, 0))
visited[N] = True

while len(queue) != 0:
    current = queue[0][0]
    count = queue[0][1]
    del queue[0]

    if current == M:
        print(count)

    if current + 1 < max_num and not visited[current+1]:
        queue.append((current+1, count +1))
        visited[current + 1] = True
    if 0<current - 1 < max_num and not visited[current-1]:
        queue.append((current-1, count +1))
        visited[current-1] = True
    if current + A < max_num and not visited[current+A]:
        queue.append((current+A, count +1))
        visited[current + A] = True
    if 0<current - A < max_num and not visited[current-A]:
        queue.append((current-A, count +1))
        visited[current -A] = True
    if current + B < max_num and not visited[current+B]:
        queue.append((current+B, count +1))
        visited[current+B] = True
    if 0<current -B < max_num and not visited[current-B]:
        queue.append((current-B, count +1))
        visited[current-B] = True
    if 0<current*A < max_num and not visited[current*A]:
        queue.append((current*A, count +1))
        visited[current*A] = True
    if 0< current*B < max_num and not visited[current*B]:
        queue.append((current*B, count +1))
        visited[current*B] = True
