# 점화식 : X[n+1] = 4X[n-1] - X[n-3]
N = int(input())
d = [0 for i in range(31)]
d[2] = 3
for i in range(4, 31, 2):
    d[i] = d[2] * d[i-2]
    for j in range(4, i, 2):
        d[i] += d[i-j] * 2
    d[i] += 2
print(d[N])

