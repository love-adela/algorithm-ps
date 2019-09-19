numbers = [int(param) for param in input().split()]

# selection sort - (1)
for i in range(len(numbers)):
    for j in range(i, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
print(' '.join(str(num) for num in numbers))

# selection sort - (2)
for i in range(len(numbers)):
    min_index = i
    for j in range(i + 1, len(numbers)):
        value = numbers[j]
        if value > numbers[min_index]:
            min_index = j
    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

