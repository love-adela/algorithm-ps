def solution(a:int, b:int)->int:
    if b <= a:
        a, b = b, a
        print(a, b)
    return sum(range(a, b+1))

# Test
m, n = map(int, input().split())
print(solution(m, n))
