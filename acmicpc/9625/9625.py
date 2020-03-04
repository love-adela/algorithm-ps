def multiply_matrix(m:tuple, n:tuple)->tuple:
    return (
            (m[0]*n[0]+m[1]*n[2]),
            (m[0]*n[1]+m[1]*n[3]),
            (m[2]*n[0]+m[3]*n[2]),
            (m[2]*n[1]+m[3]*n[3]),)

def main(n):
    if n == 0: return (1, 0, 0, 1)
    if n == 1: return (0, 1, 1, 1)
    a = main(n//2)
    a_square = multiply_matrix(a, a)
    if n % 2 == 0:
        return a_square
    else:
        return multiply_matrix(a_square, (0, 1, 1, 1))

def dp(n):
    print(main(n-1)[2], main(n-1)[3])

K = int(input())
dp(K)
