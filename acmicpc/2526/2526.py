N, P = map(int, input().split())
M = N 
order = dict()
while True:
    M = M * N % P
    if M in order:
        print(f'M: {M}')
        print(order)
        print(order[M])
        print(len(order)-order[M])
        break
    else:
        cnt = len(order)
        order[M] = cnt
