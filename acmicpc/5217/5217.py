n = int(input())
for _ in range(n):
    num = int(input())
    print(f'Pairs for {num}:', end=' ')
    for i in range(1, num//2 + 1):
        if i != num-i:
            if i!= 1:
                print(',', end=' ')
            print(i, num-i, end='')
    print()
