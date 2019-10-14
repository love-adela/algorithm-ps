import sys
read = lambda: sys.stdin.readline()
A, B, C = map(int, read().split())
BREAK_EVEN_POINT = 0

if C <= B:
    BREAK_EVEN_POINT = -1
else:
    BREAK_EVEN_POINT = A // (C-B) + 1
print(BREAK_EVEN_POINT)
