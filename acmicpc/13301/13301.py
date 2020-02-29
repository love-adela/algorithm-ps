def multiply_matrix(a, b):
    return (
        (a[0]*b[0]+a[1]*b[2]),
        (a[0]*b[1]+a[1]*b[3]),
        (a[2]*b[0]+a[3]*b[2]),
        (a[2]*b[1]+a[3]*b[3]),)

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
    return fibo_matrix(n-1)

# N = int(input())
def main(m):
    if m == 1:
        return 4
    elif m == 2:
        return 6
    else:
        return (fibo(m)[0])*4+(fibo(m-1)[0]*2)

for i in range(1, 80):
    print(main(i))
