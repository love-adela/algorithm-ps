while 1:
    p, q = map(int, input().split())
    if p == q == 0:
        break
    print(f'{p // q} {p-(p//q*q)} / {q}')
