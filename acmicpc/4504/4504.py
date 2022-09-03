n = int(input())
number = int(input())
while number:
    if number % n == 0:
        print(f'{number} is a multiple of {n}.')
    else:
        print(f'{number} is NOT a multiple of {n}.')
    number = int(input())
