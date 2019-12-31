N, K = map(int, input().split())
josephus = [i for i in range(1, N+1)]
result = []
temp = K - 1 # 6


for i in range(N):
    # 1 2 3 4 5 6 7
    if len(josephus) > temp:
        result.append(josephus.pop(temp))
        temp += K -1 # 12
        
    elif len(josephus) <= temp:
        temp %= len(josephus)
        result.append(josephus.pop(temp))
        temp += K -1 

print('<', end='')
for i in result:
    if i == result[-1]:
        print(i, end='')
    else:
        print(f'{i}, ', end='')
print('>', end='')
