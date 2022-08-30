n = int(input())

def get_sum(k:int):
    return k*(k+1)//2

def get_weight(m):
    total = 0
    for i in range(1, m+1):
        total += i*get_sum(i+1)
    return total

for i in range(n):
    print(get_weight(int(input())))

