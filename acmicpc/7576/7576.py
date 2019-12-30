def bfs(farm:list, tomatoes:list, tcount:int, urcount:int)->int:
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    is_changed = True
    count = 0
    while is_changed:
        next_tomatoes = []
        count += 1
        is_changed = False
        while tomatoes:
            tomato = tomatoes.pop()
            x, y = tomato
            for i in range(4):
                temp_x = x + dx[i]
                temp_y = y + dy[i]
                if temp_x < 0 or temp_y < 0 or temp_x >= N or temp_y >= M:
                    continue
                value = farm[temp_x][temp_y]
                if value == 0:
                    is_changed = True
                    urcount -= 1
                    if urcount == 0:
                        return count

                    farm[temp_x][temp_y] = 1
                    next_tomatoes.append((temp_x, temp_y))
        tomatoes = next_tomatoes
    return -1


M, N = map(int, input().split())
rows = []
tomato = []
tomato_count = 0
unripe_count = 0
empty_count = 0
for _ in range(N):
    row = list(map(int, input().strip().split()))
    rows.append(row)

for i in range(N):
    for j in range(M):
        value = rows[i][j]
        if value == 0:
            unripe_count += 1
        elif value == 1:
            tomato_count += 1
            tomato.append((i, j))
        elif value == -1:
            empty_count += 1
    
if tomato_count == 0:
    print(-1)
elif tomato_count + empty_count == N*M:
    print(0)
else:
    print(bfs(rows, tomato, tomato_count, unripe_count))

