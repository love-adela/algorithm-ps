import sys
T = int(sys.stdin.readline())
for t in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    print("%d%02d" % ((N-1)%H+1, (N-1)//H+1))
