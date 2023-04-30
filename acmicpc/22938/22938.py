for _ in range(1):
    x1, y1, r1 = map(int, input().split())
    x2, y2, r2 = map(int, input().split())
    if (x1, y1) == (x2, y2) and r2 != r1:
        print('YES')
    elif (x2, y2) != (x1, y1) and r2 != r1:
        print('YES')
    elif (x1, x2) != (x2, y2) and r1 == r2:
        print('YES')
    elif (x1, y1, r1) == (x2, y2, r2):
        print('YES')
    else:
        print('NO')
