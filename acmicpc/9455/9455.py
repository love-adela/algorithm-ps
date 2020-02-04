import sys
read=lambda:sys.stdin.readline()
for T in range(int(read())):
    M,N = map(int,read().split())
    grid = [list(map(int,read().split())) for i in range(M)]
    dist = 0
    for j in range(N):
        box = 0
        height = 0
        for i in range(M):
            if grid[i][j] == 1:
                box+= 1
                height+= M-i
        dist+= height-(box*(box+1)//2)
    print(dist)
