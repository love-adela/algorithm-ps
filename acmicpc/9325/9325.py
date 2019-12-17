T = int(input())
while T:
    s = int(input())
    n = int(input())
    result = s
    for _ in range(n):
        q, p = map(int, input().split())
        result += q*p
    print(result)
    T -= 1
