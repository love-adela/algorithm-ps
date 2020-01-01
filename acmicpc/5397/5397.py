import sys
from collections import deque

n=int(input())
for _ in range(n):
    l = deque()
    r = deque()
    for char in input():
        if char == '<':
            if l:
                r.appendleft(l.pop())
        elif char == '>':
            if r:
                l.append(r.popleft())
        elif char == '-':
            if l:
                l.pop()
        else:
            l.append(char)
    l.extend(r)
    print(''.join(l))
