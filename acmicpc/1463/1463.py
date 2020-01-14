import sys
sys.setrecursionlimit(10000000)

# 구해야 하는 것 : D[i] = i를 1로 만드는데 필요한 최소 연산 횟수
# 연산 1 : i가 3으로 나누어 떨어지면 3으로 나눈다 -> D[i/3] + 1

# 연산 2: i가 2로 나누어 떨어지면 2로 나눈다 -> D[i/2] + 1

# 연산 3: i에서 1을 뺀다 -> D[i-1] + 1

def get_min(n:int)->int:
    if n == 1:
        return 0 
    if d[n] > 0: return d[n]
    d[n] = get_min(n-1) + 1
    
    if n % 2 == 0:
        temp = get_min(n/2) + 1
        if d[n] > temp:
            d[n] = temp
    if n % 3 == 0:
        temp = get_min(n/3) + 1
        if d[n] > temp:
            d[n] = temp
    return d[n]

N = int(input())
d = [0] * (N+1)
print(get_min(N))
