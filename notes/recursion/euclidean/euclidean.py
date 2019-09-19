m, n = map(int, input().split())

def euclidean(m, n):
    if n == 0:
        return m
    return euclidean(n, m % n)

print(euclidean(m, n))