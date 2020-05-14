# D[n]: N을 1, 2, 3의 합으로 나타내는 방법의 수
d = [0] * 11
d[0] = 1
for i in range(1, 11):
    print(d)
    if i-1 >= 0:
        d[i] += d[i-1] 
    elif i-2 >= 0:
        d[i] += d[i-2]
    elif i-3 >= 0:
        d[i] += d[i-3]

n = int(input())
for _ in range(n):
    k = int(input())
    print(d[k])
