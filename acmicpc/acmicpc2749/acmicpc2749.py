# # fibonacci sequence
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368,

# # pisano period : 
# #   # For any integer n, the sequence of Fibonacci numbers Fi taken modulo n is periodic. 
# #   # The Pisano period, denoted π(n), is the length of the period of this sequence. 
# #   # 주기의 길이가 P면, N번째 피보나치 수를 M으로 나눈 나머지는 N%P번째 피보나치 수를 M으로 나눈 나머지와 같다.

# # n = 2 ... period : 3
# 0, 1, 1,   0, 1, 1,   0, 1, 1,   0, 1, 1,   0, 1, 1,   0, 1, 1 

# # n = 3 ... period : 8
# 0, 1, 1, 2, 0, 2, 2, 1,
# 0, 1, 1, 2, 0, 2, 2, 1, 
# 0, 1, 1, 2, 0, 2, 2, 1, 

# # n = 4 ... period : 6
# 0, 1 ,1 ,2 ,3 ,1,
# 0, 1 ,1 ,2 ,3 ,1,
# 0, 1 ,1 ,2 ,3 ,1,

# n = int(input())

def pisano_period(modulo):
    previous = 0
    current = 1

    result = 1
    while not (previous == 0 and current == 1):
        previous, current = current, (previous + current) % modulo
        result += 1
    return result 

def fibonacci(number, modulo):
    if number < 2:
        return number
    results = [1, 1]
    for _ in range(number - 2):
        results.append((results[-1] + results[-2]) % modulo)
    return results[-1]

def solution(number, modulo):
    return fibonacci(number % pisano_period(modulo), modulo)


n, m = map(int, input().split())
print(solution(n, m))