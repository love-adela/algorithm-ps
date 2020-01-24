def find_sum():
    sum = 0
    n = int(input())

    for i in range(1, n+1):
        sum = sum + i
    return sum

print(find_sum())
