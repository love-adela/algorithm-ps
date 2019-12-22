import sys

read = lambda: sys.stdin.readline().rstrip()

K = int(read())
size = [int(i) for i in read().split()]
acc = [sum(size[:i]) for i in range(K+1)]
print(acc)
