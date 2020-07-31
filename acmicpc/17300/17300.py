a = int(input())
b = [int(x) for x in input().split()]
l = [0] * 10
l[b[0]] = 1
flag = 0

for x in range(1, a):
    if l[b[x]] != 0:
        flag = 1
        break

    l[b[x]] = 1
    n, m = min(b[x-1], b[x]), max(b[x-1], b[x])

    if (n==m) or (n==1 and m==3 and l[2]==0) or (n==3 and m==9 and l[6]==0) or (n==7 and m==9 and l[8]==0) or (n==1 and m==7 and l[4]==0) or (n+m==10 and l[5]==0):
        flag = 1
        break

print("YES" if (flag == 0) else "NO")
