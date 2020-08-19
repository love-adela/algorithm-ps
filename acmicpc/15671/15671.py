# boj.kr/15671
import sys
read = lambda: sys.stdin.readline()
N = int(read())
grid = [['.' for _ in range(7)] for _ in range(7)]
grid[3][3], grid[4][4] = 'W', 'W'
grid[3][4], grid[4][3] = 'B', 'B'

dx = [-1, 0, 1, 1, 1, 0, -1, -1]
dy = [1, 1, 1, 0, -1, -1, -1, 0]

def is_captured(cur_x, cur_y, d)->bool:
    nxt_x = cur_x + dx[d]
    nxt_y = cur_y + dy[d]
    while True: 
        # 이번 nxt_x, nxt_y에서 수행할 동작(nxt_x, nxt_y는 고정)
        if not (0<nxt_x<=6 and 0<nxt_y<=6) or grid[nxt_x][nxt_y] == '.':
            return False
        if grid[nxt_x][nxt_y] == grid[cur_x][cur_y]:
            return True
        # 이번 nxt_x, nxt_y에서 해결이 안돼서 다음 칸으로 이동
        nxt_x += dx[d]
        nxt_y += dy[d]

def change_color(cur_x, cur_y, d): 
    """
    * (x, y) 위치에 돌을 놓았을 때, d 방향으로 제일 가까운 같은 색의 돌 사이의 모든 돌 뒤집기
    * (x, y) 위치에 돌을 놓았을 때, d 방향으로 같은 색의 돌이 나올 때까지 모든 돌을 뒤집기
    """
    nxt_x = cur_x + dx[d]
    nxt_y = cur_y + dy[d]

    while grid[cur_x][cur_y] != grid[nxt_x][nxt_y]:
        # 다른색일 때
        grid[nxt_x][nxt_y] = grid[cur_x][cur_y]
        nxt_x += dx[d]
        nxt_y += dy[d]

for i in range(N):
    x, y = map(int, read().split()) # for 돌 놓은 위치(고정) in 돌 로그
    if i % 2 == 0: # 돌 놓은 위치에 돌 놓기
        grid[x][y] = 'B'
    else:
        grid[x][y] = 'W'
    # 돌 놓은 위치 주변 8방향을 전부 확인하면서 같은 색 사이에 있는 돌 모두 뒤집기
    for j in range(8): # for 방향 in 주변 8방향
        if is_captured(x, y, j) : # for 돌 in 그 방향으로 제일 가까운 같은 색 사이에 있는 돌 목록
            change_color(x, y, j) # 돌 뒤집어주기

cnt_w, cnt_b = 0, 0

for i in range(1, 7):
    for j in range(1, 7):
        if grid[i][j] == 'W':
            print('W', end='')
            cnt_w += 1
        elif grid[i][j] == 'B':
            print('B', end='')
            cnt_b += 1
        else:
            print('.', end='')
    print()

print('Black' if cnt_b > cnt_w else 'White')
