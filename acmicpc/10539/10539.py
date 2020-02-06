A=int(input())
B=list(map(int, input().split()))
C=[B[0]]
for i in range(1, A):
    C.append((B[i]*(i+1))- (B[i-1]*i))
print(' '.join((map(str, C))))
