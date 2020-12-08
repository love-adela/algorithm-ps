# https://programmers.co.kr/learn/courses/30/lessons/12912
def solution(a, b):
    if a > b: a, b = b, a
    return sum(range(a, b+1))

# Test
# a, b = 3, 5
# a, b = 3, 3
a, b = 5, 3
print(solution(a, b))


