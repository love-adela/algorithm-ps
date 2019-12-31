import sys
from collections import deque

class Editor:
    def __init__(self, param:str):
        self.left_deque = deque(param)
        self.right_deque = deque()

    # 커서를 왼쪽으로 한 칸 옮김
    def move_left(self):
        if self.left_deque:
            self.right_deque.appendleft(self.left_deque.pop())
    
    # 커서를 오른쪽으로 한 칸 옮김
    def move_right(self):
        if self.right_deque:
            self.left_deque.append(self.right_deque.popleft())

    # 커서 왼쪽에 있는 문자 삭제
    def delete(self):
        if self.left_deque:
            self.left_deque.pop()
    
    # 문자를 커서 왼쪽에 추가
    def add(self, character):
        self.left_deque.append(character)

editor = Editor(sys.stdin.readline().strip())

M = int(sys.stdin.readline().strip())

while M:
    command = sys.stdin.readline().strip()
    if command[0] == 'L':
        editor.move_left()
    elif command[0] == 'D':
        editor.move_right()
    elif command[0] == 'B':
        editor.delete()
    else:
        editor.add(command[2])
    M -=1
print(''.join(editor.left_deque) + ''.join(editor.right_deque))
