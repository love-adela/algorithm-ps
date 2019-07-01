import sys

read = lambda: sys.stdin.readline().split()

def euclidean(a, b):
    if b == 0:
        return a
    return euclidean(b, a % b)

def lcm(a, b):
    return int(a * b / euclidean(a, b))

m, n = map(int, read())
print(lcm(m, n))
