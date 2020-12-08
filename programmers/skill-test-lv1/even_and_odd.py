# https://programmers.co.kr/learn/courses/30/lessons/12937
def solution(num:int)->str:
    return 'Even' if num % 2 == 0 else 'Odd'

# Test
print(solution(60))
print(solution(15))
print(solution(3))
print(solution(4))

