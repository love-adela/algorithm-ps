import math
N, K = map(int, input().split())
girls, boys = [], [] 
while N:
    S, Y = map(int, input().split())
    if S == 0:
        girls.append(Y)
    else:
        boys.append(Y)
    N -= 1
count = 0
girls = sorted(girls)
boys = sorted(boys)
for i in range(6):
    count += math.ceil(girls.count(i+1)/K)
    count += math.ceil(boys.count(i+1)/K)
print(count)
