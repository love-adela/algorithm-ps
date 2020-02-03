N = int(input())
paper = [[0]*101 for _ in range(101)]
count = [0]*(N+1)
for n in range(1, N+1):
    data = list(map(int, input().split()))
    for i in range(data[0], data[0]+data[2]):
        for j in range(data[1], data[1]+data[3]):
            paper[i][j] = n

for e in paper:
    for a in e:
        if a:
            count[a] += 1

for e in count[1:]:
    print(e)
