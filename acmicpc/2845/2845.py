L, P = map(int, input().split())
n = L*P
d = [str(i-n) for i in map(int,input().split())]
print(' '.join(d))
