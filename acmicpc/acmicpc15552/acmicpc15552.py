import sys

read = lambda: sys.stdin.readline().strip()

n = int(read())
for _ in range(n):
    a, b = map(int, read().split())
    # print(a, b)    
    print(a + b)

