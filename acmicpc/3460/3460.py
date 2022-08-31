t = int(input())
for _ in range(t):
    n = bin(int(input()))[2:]
    for index, value in enumerate(n[::-1]):
        if value == '1':
            print(index, end =' ')
