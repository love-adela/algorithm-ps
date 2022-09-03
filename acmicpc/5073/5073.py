while 1:
    p, q, r = sorted(map(int, input().split()))
    if p == q == r == 0:
        break
    elif p + q <= r:
        print('Invalid')
    elif (p == q and q != r) or (q == r and p != q) or (p == r and p!=q):
        print('Isosceles')
    elif p == q == r:
        print('Equilateral')
    elif p != q != r:
        print('Scalene')
