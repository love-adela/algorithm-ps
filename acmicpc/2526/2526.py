N, P = map(int, input().split())
M = N 
order = dict()
while True:
    M = M * N % P
    if M in order:
        print(len(order)-order[M])
        break
    else:
        cnt = len(order)
        order[M] = cnt
