from sys import stdin

m, n = map(int, input().split())
status = stdin.read().split() 

def dijkstra():
    COST = [[1e4]*m for _ in range(n)]
    COST[0][0] = 0
    deque = [(0, 0)]

    while True:
        x, y = deque.pop(0) 
        if x == m-1 and y == n-1:
            return COST[n-1][m-1]

        cost = COST[y][x]
        for x, y in [(x, y-1), (x-1, y), (x+1, y), (x, y+1)]:
            if not (0 <= x < m and 0 <= y < n):
                continue

            is_wall = status[y][x] == '1'
            new_cost = cost + (1 if is_wall else 0)

            if COST[y][x] <= new_cost:
                continue

            COST[y][x] = new_cost
            if is_wall:
                deque.append((x, y))
            else:
                deque.insert(0, (x, y))
print(dijkstra())
