N, M = map(int, input().split())
grid = [input() for _ in range(N)]
max_length = min(N, M)

def is_square(n):
    for i in range(N-n+1):
        for j in range(M-n+1):
            if is_same(n, i, j):
                return True
    return False

def is_same(k, x, y):
    if grid[x][y] == grid[x][y+k-1] == grid[x+k-1][y] == grid[x+k-1][y+k-1]:
        return True
    return False

for length in range(max_length, 1, -1):
    if is_square(length):
        print(length ** 2)
        break
else:
    print(1)
