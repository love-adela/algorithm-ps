def dp(is_open:list, k:int, n:int):
    if k == n+1:
        print(is_open.count(1))
        return
    for i in range(k-1, n, k):
        if is_open[i] == 0: is_open[i] = 1
        elif is_open[i] == 1: is_open[i] = 0
    dp(is_open, k+1, n)

T = int(input())
for i in range(T):
    cells = int(input())
    is_open = [0] * cells
    dp(is_open, 1, cells)

