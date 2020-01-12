g=lambda n,k:sum(n//k**i for i in range(1,31))
n,m=map(int,input().split())
l=n-m
h=lambda k:g(n,k)-g(m,k)-g(l,k)
print(min(h(2),h(5)))
