m, n = map(int, input().split())

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(m, n))

def lcm(a, b):
    return int(a * b / gcd(a, b))

print(lcm(m,n))
