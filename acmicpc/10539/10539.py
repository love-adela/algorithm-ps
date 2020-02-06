A=int(input())
B=list(map(int, input().split()))
C=[]
for i in range(A):
    C.append(B[i+1]*(i+1)- B[i-1])
print(C)
