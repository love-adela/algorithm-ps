import sys
class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, value:int):
        return self.items.append(value)

    def pop(self):
        if not self.items:
            return -1
        else:
            return self.items.pop()

    def get_size(self):
        return len(self.items)

    def is_empty(self):
        if bool(self.items) is True:
            return 0 
        else:
            return 1

    def get_top(self):
        if not self.items:
            return -1
        elif self.items:
            return self.items[-1]

stack = Stack()
N = int(input())
for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        stack.push(command[1])
    elif command[0] == 'pop':
        print(stack.pop())
    elif command[0] == 'size':
        print(stack.get_size())
    elif command[0] == 'empty':
        print(stack.is_empty())
    else:
        print(stack.get_top())
