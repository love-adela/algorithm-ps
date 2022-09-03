cnt = int(input())
for _ in range(cnt):
    total = 0
    a, b, c, d, e = map(int, input().split())
    total = 350.34 * a + 230.90 * b + 190.55 * c + 125.30 * d + 180.90 * e
    print(f'$%.2f' % total)
