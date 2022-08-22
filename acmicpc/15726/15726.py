a, b, c = map(int, input().split())

if (a * b) / c > (a / b) *c:
    print(int(a*b/c))
else:
    print(int(a/b*c))
