import sys
N = int(sys.stdin.readline())
for _ in range(N):
    R, S = sys.stdin.readline().rstrip().split(' ')
    for l in S:
        print(l*int(R), end='')
    print()
