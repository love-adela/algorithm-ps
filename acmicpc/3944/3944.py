import sys
read = sys.stdin.readline
for _ in range(int(read())):
    B,D=read().split()
    print(sum(map(int,D))%(int(B)-1))
    # D를 바로 Integer casting해버리면 'int' object는 iterable 하지 않기 때문에 sum연산이 되지 않는다. 
