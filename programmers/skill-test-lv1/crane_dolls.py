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

stack = []
for move in moves:
    stack.append(get_top(board, move))

# Remove None
# new_stack = [item for item in stack if item]
new_stack = [1, 4, 2, 2, 4, 1, 1]

"""
이 풀이의 문제점
- 맨 위에 겹친 두개 아이템씩 없애야 함
- 맨 앞부터 겹쳐진 아이템 찾아서 겹친게 3개 이상 생길 수 있음
    - 예시: [1, 4, 2, 2, 4, 1, 1]
"""
def get_radix(stack:list):
    for i in range(len(stack)-1):
        if stack[i] == stack[i+1]:
            return stack[i]

def remove_radix_values(new_stack):
    radix = get_radix(new_stack)
    if not radix:
        return new_stack
    new_stack = [item for item in new_stack if item != radix]
    print(new_stack)
    return remove_radix_values(new_stack)

res_stack = remove_radix_values(new_stack)
print(len(new_stack)-len(res_stack))
