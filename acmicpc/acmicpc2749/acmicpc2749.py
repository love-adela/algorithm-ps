# # pisano period : 
  # For any integer n, the sequence of Fibonacci numbers taken modulo n is periodic. 
  # 주기의 길이가 P면, N번째 피보나치 수를 M으로 나눈 나머지는 N%P번째 피보나치 수를 M으로 나눈 나머지와 같다.
  # M은 10 ** k 일 때, 주기는 항상 15 * 10 ** (k -1)이 된다.

# 문제 풀이 힌트 
  # 일관성을 잃지 않고 정의역 (Domain)을 확장시킬 것 => '해석적 확장' 
  # 행렬 곱 연산 활용하기

def pisano_period(n:int) -> int:
    fibo = [0, 1]
    quotient = 1000000
    period = int(quotient / 10 * 15)
    index = 2

    while index < period:
        fibo.append(fibo[index-1] + fibo[index-2])
        fibo[index] %= quotient
        index += 1
    return fibo[n%period]

n = int(input())
print(pisano_period(n))


def matrix_fibo(n:int) -> int:
    SIZE = 2
    ZERO = [[1, 0], [0, 1]] # 단위행렬
    BASE = [[1, 1], [1, 0]]
    
    def multiply_matrix(a, b, size=SIZE):
        new = [[0 for _ in range(size)] for _ in range(size)]

        for i in range(size):
            for j in range(size):
                for k in range(size):
                    new[i][j] += a[i][k] * b[k][j]
        return new

    def get_nth(n):
        matrix = ZERO.copy()
        k = 0
        tmp = BASE.copy()

        while 2 ** k <= n:
            if n & (1 << k) != 0:
                matrix = multiply_matrix(matrix, tmp)
            k += 1
            tmp = multiply_matrix(tmp, tmp)

        return matrix

    return get_nth(n)[1][0]
                    
def fibonacci_matrix(n: int, mod: int) -> int:
    arr, constant = [[1, 0], [0, 1]], [[1, 1], [1, 0]]
    while n > 0:
        if n % 2 == 1:
            arr = multiply_matrix(arr, constant, mod)
        constant = multiply_matrix(constant, constant, mod)
        n = n // 2
    return arr[0][0]

def multiply_matrix(matrix_a, matrix_b, mod) -> list:
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] = (result[i][j] + matrix_a[i][k] * matrix_b[k][j]) % mod
    return result

mod = 10 ** 6
print(fibonacci_matrix(int(input()) - 1, mod))

