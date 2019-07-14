# 행렬로 푸는 풀이: 최적해
def fibo_matrix(n):
    if n < 0:
        print("정수를 입력하세요")
    
    current_item = 0
    next_item = 1
    for _ in range(n):
        (current_item, next_item) = (next_item, current_item + next_item)
    return current_item

print(fibo_matrix(7))

# Memoization 하는 풀이 : O(n)
def fibo(n):
    # Base Case
    if n == 0:
        return 1
    if n == 1:
        return 1
    dict = {}
    if n in dict:
        return dict[n] # memoization
    answer = fibo(n - 1) + fibo(n - 2)
    dict[n] = answer
    return answer

