n = int(input())
def divisor(x, y, z=0):
    if z == 0:
        min_number = min(x, y)
    else:
        min_number = min(x, y, z)
    for i in range(1, min_number):
        if x % i == 0 and y % i and z % i == 0:
            print(i)

if n == 2:
    a, b = map(int, input().split())
    divisor(a, b)

if n == 3:
    a, b, c = map(int, input().split())
    divisor(a, b, c)
