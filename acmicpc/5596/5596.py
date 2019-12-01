mk = list(map(int, input().split()))
ms = list(map(int, input().split()))

sum_mk = sum(mk)
sum_ms = sum(ms)
if sum_mk >= sum_ms:
    print(sum_mk)
else:
    print(sum_ms)
