# https://programmers.co.kr/learn/courses/30/lessons/64061
def get_top(board, move):
    for i in range(len(board)):
        if board[i][move-1] != 0:
            res = board[i][move-1]
            board[i][move-1] = 0
            return res

# Test
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

# result = 4
stack = []
for move in moves:
    stack.append(get_top(board, move))

# Remove None
new_stack = [item for item in stack if item]

def get_radix(stack:list):
    for i in range(len(stack)-1):
        if stack[i] == stack[i+1]:
            return stack[i]

def remove_radix_values(new_stack):
    radix = get_radix(new_stack)
    if not radix:
        return new_stack
    new_stack = [item for item in new_stack if item != radix]
    return remove_radix_values(new_stack)

res_stack = remove_radix_values(new_stack)
print(len(new_stack)-len(res_stack))
