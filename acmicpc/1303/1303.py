N, M = map(int, input().split())
coordinates = [[param for param in input()] for _ in range(M)] 
visited = [[False] * N for _ in range(M)]
white, black = 0, 0

def bfs(x, y, curr):
    candidates = [(x, y)]
    cnt = 1 

    while candidates:
        _, *candidates = candidates
        print(candidates)
        for delta_x, delta_y in (-1, 0), (1, 0), (0, -1), (0, 1):
            new_x, new_y = x+delta_x, y+delta_y
            if 0 <=new_x<M and 0<= new_y < N:
                if not visited[new_x][new_y] and coordinates[new_x][new_y] == curr:
                    visited[new_x][new_y] = True
                    candidates.append((new_x, new_y))
                    cnt += 1
    return cnt

for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            res = bfs(i, j, coordinates[i][j])
            if coordinates[i][j] == 'W': white += res**2
            else: black+= res**2

print(white, black)

