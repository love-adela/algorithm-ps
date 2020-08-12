N = int(input())
grid = [['.' for _ in range(N+1)] for _ in range(N+1)]
grid[3][3], grid[4][4] = 'W', 'W'
grid[3][4], grid[4][3] = 'B', 'B'

dx = [-1, 0, 1, 1, 1, 0, -1, -1]
dy = [1, 1,1 , 0, -1, -1, -1, 0]

def is_captured(cur_x, cur_y, nxt_x, nxt_y, d)->bool:
    if not (0<=nxt_x<6 and 0<=nxt_y<6) or grid[nxt_x][nxt_y] == '.':
        return False
    if grid[nxt_x][nxt_y] == grid[cur_x][cur_y]:
        return True
    return is_captured(cur_x, cur_y, nxt_x, nxt_y, d)

for i in range(N):
    x, y = map(int, input().split())
    if i % 2 == 0:
        grid[x][y] = 'B'
    else:
        grid[x][y] = 'W'
    for j in range(8):
        is_captured(x, y, x+dx[j], y+dy[j], j)

cnt_w, cnt_b = 0, 0

for i in range(1, N+1):
    for j in range(1, N+1):
        if grid[i][j] == 'W':
            print('W')
            cnt_w += 1
        elif grid[i][j] == 'B':
            print('B')
            cnt_b += 1
        else:
            print('.')

if cnt_w > cnt_b: print('White')
else: print('Black')
