from decimal import getcontext, Decimal 
import sys
getcontext().prec = 21 
read = lambda: sys.stdin.readline()

def get_decimal(t:int):
    cost = [[0, 0, 0]]
    for _ in range(4):
        params = list(map(Decimal, read().split()))
        cost.append(params)
    total = 0
    for i in range(4):
        distance = 0
        for j in range(3):
            distance += ((cost[i+1][j] - cost[i][j])**2)
        total += (Decimal(distance).sqrt())
    return total 

T = int(input())
for _ in range(T):
    time = int(read())
    answer = get_decimal(time)
    if time >= answer: print('YES')
    else: print('NO')
