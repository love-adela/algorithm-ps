dict = {}

# 1. 재귀함수를 이용하는 풀이


def fibo(n):
    # Base Case
    if n == 0:
        return 1
    if n == 1:
        return 1

    if n in dict:
        return dict[n] # memoization

    answer = fibo(n - 1) + fibo(n - 2)
    dict[n] = answer
    return answer
# 시간복잡도 : O(n)

# 2. while문 이용하는 풀이


def gcd_while(a, b):
    previous = 1
    current = 1
    i = 0
    while i < 20:
        temp = previous
        previous = current
        current = temp + current
        i += 1

# print(fibo(10))

example = int(input("입력하세여"))

for i in range(0, example):
    answer = fibo(i)
    print(f"fibo({i}) = {answer}")
# 시간복잡도 : O(2 ** n)



