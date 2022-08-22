while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    if m > n: print('Yes')
    else: print('No')
