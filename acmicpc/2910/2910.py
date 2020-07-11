N, C = map(int, input().split())
sequence = list(map(int, input().split()))
frequency = dict() # key: 숫자, value : 빈도

for number in sequence:
    if number in frequency:
        params = frequency[number]
        frequency[number]+=1
    else:
        frequency[number] = 1

params = sorted(frequency.items(), key = lambda x:x[1], reverse=True)

for param in params:
    for _ in range(param[1]):
        print(param[0], end=' ')
