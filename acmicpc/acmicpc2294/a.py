import sys
read = lambda : sys.stdin.readline().strip()
write = lambda x: sys.stdout.write(str(x)+ "\n")

n,k=map(int, read().split())
dp=[0]+[sys.maxsize]*(k)
c = [int(read()) for _ in range(n)]

for i in c:
    for j in range(i,k+1):
        dp[j]=min(dp[j],dp[j-i]+1)

if dp[k]==10001:
    write(-1)
else:
    write(dp[k])

