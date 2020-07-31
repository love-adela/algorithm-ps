import sys
N = int(sys.stdin.readline())
grid = [list(map(int, input().split())) for i in range(N)]

white, blue = 0, 0

def divide_and_conquer(x, y, n):
    global white, blue
    is_same = grid[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if is_same != grid[i][j]:
                divide_and_conquer(x, y, n//2)
                divide_and_conquer(x, y+n//2, n//2)
                divide_and_conquer(x+n//2, y, n//2)
                divide_and_conquer(x+n//2, y+n//2, n//2)
                return 
    if is_same == 0:
        white += 1
        return
    else:
        blue += 1
        return

divide_and_conquer(0, 0, N)
print(white)
print(blue)

