def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

number_of_cases = int(input())
number_of_zero = [1, 0, 1]
number_of_one = [0, 1, 1]

def count_numbers(n: int):
    length = len(number_of_zero)
    if length <= n:
        for i in range(length, n+1):
            number_of_zero.append(number_of_zero[i-1] + number_of_zero[i-2])
            number_of_one.append(number_of_one[i-1] + number_of_one[i-2])
            print(f"{number_of_zero[n]}",f"{number_of_one[n]}")

for i in range(number_of_cases):
    case = int(input())
    count_numbers(case)


# fibonacci(0) = 0
# fibonacci(1) = 1
# # fibonacci(2) = fibonacci(1) + fibonacci(0) = 0 + 1
# fibonacci(3) = fibonacci(2) + fibonacci(1) = 0 + 1 + 1 = 2
