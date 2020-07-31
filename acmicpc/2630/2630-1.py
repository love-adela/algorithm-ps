import sys
input = sys.stdinn.readline
n = int(input())

grid = [[*map(int, input().split())] for i in range(n)]

def divide_grid_into_quarters(x, y, size):
    new_x = x + size
    new_y = y + size
    yield x,  y
    yield new_x, y
    yield x, new_y
    yield new_x, new_y

def conquer(x, y, size):
    if size == 1:
        return (0, 1) if paper[x][y] else (1, 0)
    a, b = 0, 0
    new_size = size // 2
    for u, v in divide_grid_into_quarters(x, y, new_size):
        new_a, new_b = conquer(u, v, new_size)
        a += new_a
        b += new_b
    if a == 0:
        return 0, 1
    elif b == 0:
        return 1, 0
    return a, b

a, b = conquer(0, 0, n)
print(a)
print(b)
