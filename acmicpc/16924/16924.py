def count_cross(i, j):
    if grid[i][j] == '.':
        return
    for d in range(1, 123):
        for new_i, new_j in (i-d, j), (i+d, j), (i, j-d), (i, j+d):
            if not (0 <= new_i < N and 0 <= new_j < M) or grid[new_i][new_j] == '.':
                break
        else: continue
        break
    if d >= 2: crosses.append((i, j, d-1))

N, M= map(int, input().split())
grid = [input() for i in range(N)]
crosses = []
for i in range(N):
    for j in range(M): count_cross(i, j)

new_grid = [['.']*M for i in range(N)]
for i, j, d in crosses:
    new_grid[i][j] = '*'
    for new_d in range(1, d+1):
        for new_i, new_j in (i-new_d, j), (i+new_d, j), (i, j-new_d), (i, j+new_d):
            new_grid[new_i][new_j] = '*'

new_grid = [''.join(row) for row in new_grid]
if grid != new_grid:
    print(-1)
else:
    print(len(crosses))
    for i, j, d in crosses:
        print(i+1, j+1, d)
