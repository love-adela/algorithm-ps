# sum(1에서 N까지의 피보나치 수) = N+2 번째 피보나치 수 - 1
import sys
a, b = map(int, sys.stdin.readline().split())
def multiply_matrix(m, n):
    MOD= 1000000000
    return (
            (m[0]*n[0]+m[1]*n[2])%MOD,
            (m[0]*n[1]+m[1]*n[3])%MOD,
            (m[2]*n[0]+m[3]*n[2])%MOD,
            (m[2]*n[1]+m[3]*n[3])%MOD,)

def fibo_matrix(n):
    if n == 0: return (1, 0, 0, 1)
    if n == 1: return (1, 1, 1, 0)
    a = fibo_matrix(n//2)
    a_square = multiply_matrix(a, a)
    if n % 2 == 0:
        return a_square
    else: return multiply_matrix(a_square, (1, 1, 1, 0))

def fibo(n):
    return fibo_matrix(n-1)[0]
print(((fibo(b+2)-1) - (fibo(a+1)-1))%1000000000)
