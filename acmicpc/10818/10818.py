import sys

read = lambda: sys.stdin.readline()

n = int(read())
numbers = list(map(int, input().split()))
print(f'{min(numbers)} {max(numbers)}')
