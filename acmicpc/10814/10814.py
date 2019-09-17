import sys
N = int(sys.stdin.readline())
info = list()
for i in range(N):
    age, name = sys.stdin.readline().split()
    info.append([int(age), name, i])
info.sort(key=lambda x:(x[0], x[2]))
for param in info:
    print(param[0], param[1])
