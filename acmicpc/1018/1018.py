import sys

n, m = map(int, sys.stdin.readline().split())

b = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(n):
    status = sys.stdin.readline().strip()
    for j in range(m):
        temp = (i+j) % 2 
        if status[j] == 'B':
            temp = 1-temp
        b[i+1][j+1] = b[i][j+1] + b[i+1][j] - b[i][j] + temp

max_value = 32

for i in range(8, n+1):
    for j in range(8, m+1):
        x = b[i][j] + b[i-8][j-8] - b[i][j-8] - b[i-8][j]
        if x > max_value:
            x = 64-x
        if x < max_value:
            max_value = x
print(max_value)

