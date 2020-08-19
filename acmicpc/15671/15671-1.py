# boj.kr/15671
import sys
def flip(cur_x, cur_y, dx, dy, player_color):
    result = [(cur_x, cur_y)]
    while True:
        cur_x += dx
        cur_y += dy
        if not (0<=cur_x<6 and 0<=cur_y<6): 
            return []
        if grid[cur_x][cur_y] == 46:
            return []
        if grid[cur_x][cur_y] == player_color:
            return result
        result.append((cur_x, cur_y))

def place(x, y, player_color):
    for dx, dy in (1,0), (-1,0), (0,1), (0,-1),\
        (-1,1), (1,-1), (1,1), (-1,-1):
            for new_x, new_y in flip(x, y, dx, dy, player_color):
                grid[new_x][new_y] = player_color

input = lambda: sys.stdin.readline()
get_game_log = lambda:map(int, input().split())
B = 66
W = 87
grid = [[46]* 6 for _ in range(6)]
grid[2][2] = grid[3][3] = W
grid[2][3] = grid[3][2] = B
player = B # 선 : 흑돌

cnt_black, cnt_white = 0, 0

for _ in range(int(input())):
    x, y = get_game_log()
    x -= 1; y -= 1
    place(x, y, player)
    player = W+B-player

for row in grid:
    for elem in row:
        if elem == B:
            cnt_black +=1 
        if elem == W:
            cnt_white += 1
        print(chr(elem), end='')
    print()
print('White' if cnt_white > cnt_black else 'Black')


