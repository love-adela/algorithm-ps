N, P = map(int, input().split())
M = N 
A = set()
B = set()

for i in range(P*2):
    M = M * N % P
    if M not in A:
        A.add(M)
    else:
        B.add(M)
print(len(B))
