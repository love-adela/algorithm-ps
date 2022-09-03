cnt = 0
while True:
    n = int(input())
    cnt += 1
    if n == 0:
        break
    if n % 2 != 0:
        print(f'{cnt}. odd {n//2}')
    else:
        print(f'{cnt}. even {n//2}')

