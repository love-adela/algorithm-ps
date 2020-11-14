N = int(input())
K = int(input())

grid = [[0]*N for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ul, ll = (N//2)-1, (N//2)-1
dl, rl = (N//2)+1, (N//2)+1

i, j = N//2, N//2
value = 1
grid[i][j] = value
 
d = 0
p = [-1, -1]

while True:
    i += dx[d]
    j += dy[d]
    value += 1
    if value == K:
        p = [i+1, j+1]
    if i == -1 and j == 0:
        break
    grid[i][j] = value
    if i == ul:
        ul -= 1
        d += 1
        d %= 4

    if i == dl:
        dl += 1
        d += 1
        d %= 4
    
    if j == rl:
        rl += 1
        d += 1
        d %= 4

    if j == ll:
        ll -= 1
        d += 1
        d %= 4

for elem in grid:
    print(*elem)
print(*p)
