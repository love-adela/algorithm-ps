class Stack(object):
    def __init__(self):
        self.container = []
        self.count = 0

    def push(self, value):
        self.container.append(value)
        self.count += 1

    def pop(self):
        if self.is_empty():
            return -1
        self.count -= 1
        return self.container.pop()

    def size(self):
        return self.count

    def is_empty(self):
        if self.count == 0:
            return 1
        return 0

    def peek(self):
        if self.is_empty():
            return -1
        return self.container[-1]

import sys
s = Stack()
string = input()
result = ''
flag = False
for c in string:
    if c == '<':
        while not s.is_empty():
            result += s.pop()
        result += c
        flag = True
    elif c == '>':
        result += c
        flag = False
    elif flag:
        result += c
    elif c == ' ':
        while not s.is_empty():
            result += s.pop()
        result += c
    else:
        s.push(c)

while not s.is_empty():
    result += s.pop()
print(result)

