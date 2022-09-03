n = int(input())
cnt_a, cnt_b = 0, 0
for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        cnt_a += 1
    elif b > a:
        cnt_b += 1
print(cnt_a, cnt_b)
