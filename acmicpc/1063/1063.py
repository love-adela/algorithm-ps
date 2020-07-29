king, stone, n = input().split()

king_x, king_y = king[0], king[1]
stone_x, stone_y = stone[0], stone[1]

def is_in_range(x:str, y:str)->bool:
    return ('A'<= x <= 'H') and ('1' <= y <= '8')

move = {'R': (1, 0), 'L': (-1, 0), 'B': (0, -1), 'T': (0, 1), 'RT': (1, 1), 'LT': (-1, 1), 'RB': (1, -1), 'LB': (-1, -1)}

for i in range(int(n)):
    command = input()
    x, y = move[command][0], move[command][1]

    # 킹이 이동할 수 없는 경우
    if not is_in_range(chr(ord(king_x) + x), chr(ord(king_y) + y)):
        continue
    # 킹이 돌의 위치로 이동한 경우
    if chr(ord(king_x) + x) == stone_x and chr(ord(king_y) + y) == stone_y:
        # 돌이 이동할 수 없는 경우
        if not is_in_range(chr(ord(stone_x)+x), chr(ord(stone_y) +y)): continue
        stone_x = chr(ord(stone_x) + x)
        stone_y = chr(ord(stone_y) + y)
    king_x = chr(ord(king_x) + x)
    king_y = chr(ord(king_y) + y)

print(f'{king_x}{king_y}')
print(f'{stone_x}{stone_y}')
