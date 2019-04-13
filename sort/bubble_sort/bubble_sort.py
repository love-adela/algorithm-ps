numbers = [int(param) for param in input().split(' ')]

# bubble sort
for i in range(len(numbers)):
    for iteration in range(len(numbers) - (1 + i)):
        if numbers[iteration] > numbers[iteration + 1]:
            numbers[iteration], numbers[iteration + 1] = numbers[iteration + 1], numbers[iteration]
print(' '.join(str(num) for num in numbers))
