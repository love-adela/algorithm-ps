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