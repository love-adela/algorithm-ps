def solution(board, moves):
    stack = []
    cnt = 0
    for move in moves:
        for i in range(len(board)):
            if board[i][move -1] != 0:
                res = board[i][move-1]
                board[i][move-1] = 0
                if len(stack) == 0 or res != stack[-1]:
                    stack.append(res)
                else:
                    cnt += 1
                    del stack[-1]
                break
    return cnt *2
