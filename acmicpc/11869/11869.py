M = int(input())
P = list(map(int, input().split()))

answer = 0
for i in range(M):
    answer ^= P[i]
if answer != 0: print('koosaga')
else: print('cubelover')
