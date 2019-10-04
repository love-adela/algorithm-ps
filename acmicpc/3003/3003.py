p = [int(i) for i in input().split()]
c = [1, 1, 2, 2, 2, 8]
print(' '.join([str(c[i] - p[i]) for i in range(6)]))
