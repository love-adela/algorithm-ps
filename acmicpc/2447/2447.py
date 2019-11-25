a=int(input())
def s(n):
    if n==3:return['***','* *','***']
    x=s(n//3)
    y=list(zip(x,x,x))
    for i in range(len(y)):
        y[i]=''.join(y[i])
    z=list(zip(x,[' '*(n//3)]*(n//3),x))
    for i in range(len(z)):
        z[i]=''.join(z[i])
    return y+z+y
print('\n'.join(s(a)))
