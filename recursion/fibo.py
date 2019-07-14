# 행렬로 푸는 풀이: 최적해
    # a[0] a[1]      b[0] b[1]
    # a[2] a[3]      b[2] b[3]

def multiply_matrix(a, b):
    return (
            a[0]*b[0] + a[1]*b[2], 
            a[0]*b[1] + a[1]*b[3],
            a[2]*b[0] + a[3]*b[2],
            a[2]*b[1] + a[3]*b[3]
            )

def fibo_matrix(n):
    if n == 0:
        return (1, 0, 0, 1)
    if n == 1:
        return (1, 1, 1, 0)

    a = fibo_matrix(n//2)
    a_square = multiply_matrix(a, a)
    if n % 2 == 0:
        return a_square 
    else:
        return multiply_matrix(a_square, (1, 1, 1, 0))

def fibo(n):
    if n == 0:
        return 0
    return fibo_matrix(n-1)[0]

print(fibo(0))
print(fibo(1))
print(fibo(2))
print(fibo(3))
print(fibo(4))
print(fibo(5))
print(fibo(6))
print(fibo(7))
print(fibo(8))
print(fibo(9))
