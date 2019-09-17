N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]
ranks = [1] * N

for i in range(len(info)):
    for j in range(len(info)):
        if info[i][0] != info[j][0] and info[i][1] != info[j][1]:
            if info[i][0] > info[j][0] and info[i][1] > info[j][1]:
                ranks[j] += 1

print(*ranks)
