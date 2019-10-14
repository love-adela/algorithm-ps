K, N, M = map(int, input().split())
cost = K*N
if cost >= M:
    print(cost-M)
else:
    print(0)
