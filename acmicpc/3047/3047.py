numbers = sorted([int(param) for param in input().split()])

char = input()
for c in char:
    if c == 'A':
        print(numbers[0], end =' ')
    elif c == 'B':
        print(numbers[1], end = ' ')
    elif c == 'C':
        print(numbers[2], end = ' ')

