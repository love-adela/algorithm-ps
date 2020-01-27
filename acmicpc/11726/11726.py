n = int(input())
def multiply_matrix(a, b):
    MOD = 10007
    return (
        (a[0]*b[0]+a[1]*b[2])%MOD,
        (a[0]*b[1]+a[1]*b[3])%MOD,
        (a[2]*b[0]+a[3]*b[2])%MOD,
        (a[2]*b[1]+a[3]*b[3])%MOD,)

def fibo_matrix(n):
    if n == 0: return (1, 0, 0, 1)
    if n == 1: return (1, 1, 1, 0)
    a = fibo_matrix(n//2)
    a_square = multiply_matrix(a,a)
    if n %2==0: 
        return a_square
    else:
        return multiply_matrix(a_square, (1, 1, 1, 0))

def fibo(n):
    return fibo_matrix((n-1)%2000000016)[0]
fibo = fibo(n+1)
print(fibo)
