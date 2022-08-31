numbers = sorted([int(param) for param in input().split()])

if numbers[2] - numbers[1] == numbers[1] - numbers[0]:
    print(numbers[2] * 2 - numbers[1])
elif numbers[1] - numbers[0] > numbers[2] - numbers[1]:
    print(numbers[1] * 2 - numbers[2])
else:
    print(numbers[1] * 2 - numbers[0])

