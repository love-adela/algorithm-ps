import sys
read = sys.stdin.readline
for _ in range(int(read())):
    B,D=read().split()
    print(sum(map(int,D))%(int(B)-1))
