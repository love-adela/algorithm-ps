import sys
n = int(sys.stdin.readline())
result = 1
for i in range(n):
    y = int(sys.stdin.readline())
    result = result + y -1
print(result)

