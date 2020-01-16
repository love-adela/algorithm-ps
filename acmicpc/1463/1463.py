# 구해야 하는 것 : D[i] = i를 1로 만드는데 필요한 최소 연산 횟수
# 연산 1 : i가 3으로 나누어 떨어지면 3으로 나눈다 -> D[i/3] + 1

# 연산 2: i가 2로 나누어 떨어지면 2로 나눈다 -> D[i/2] + 1

# 연산 3: i에서 1을 뺀다 -> D[i-1] + 1
memo = dict()
def get_min(n:int)->int:
    if n in memo:
        return memo[n] 
    if n < 2: result = 0
    else:
        x = get_min(n//2)+n%2+1


N = int(input())
d = [0] * (N+1)
print(get_min(N))
