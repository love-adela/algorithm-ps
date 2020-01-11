m,c=4000000,0
check=[True]*m
for i in range(3,int(m**0.5)+1,2):
 if check[i]:check[i*i::2*i]=[False]*((m-i*i-1)//(2*i)+1)
x=[2]+[i for i in range(3,m,2) if check[i]]
a,b,d=map(int,input().split())
d=str(d)
for i in x:
 if i>=a and i<=b:
  if d in str(i):c+=1
print(c)
