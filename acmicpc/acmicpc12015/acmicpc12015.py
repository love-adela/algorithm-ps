import sys
from bisect import bisect_left

read = lambda: sys.stdin.readline().strip()
read()

m = map(int, input().split())
arr = [next(m)]
for i in m:
    if arr[-1] < i:
        arr.append(i)
    else:
        arr[bisect_left(arr, i)] = i
print(len(arr))
