n = int(input())
result = 0
result_list = []
for _ in range(n):
    a, b, c = map(int, input().split())
    if a == b == c:
        result = 10000 + a * 1000
    elif a == b or a == c:
        result = 1000 + a * 100
    elif b == c:
        result = 1000 + c * 100
    else:
        result = max(a, b, c) * 100
    result_list.append(result)
print(max(result_list))
