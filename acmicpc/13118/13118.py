points = list(map(int, input().split()))
x, y, r = map(int, input().split())

if x in points:
    print(points.index(x) + 1)
else:
    print(0)
