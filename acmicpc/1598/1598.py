def num2coord(n):
    x = (n-1)//4
    y = (n-1)%4
    return x, y

a, b = map(int, input().split())
ax, ay = num2coord(a)
bx, by = num2coord(b)
print(abs(ax-bx) + abs(ay-by))
