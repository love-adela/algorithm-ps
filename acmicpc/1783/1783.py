N, M = map(int, input().split())
count = 0

if N is 1:
    count = 1
elif N is 2:
    count = min(4, (M+1)//2)
elif M < 7:
    count = min(M, 4)
else:
    count =M -2 # 5 + m -7

print(count)
