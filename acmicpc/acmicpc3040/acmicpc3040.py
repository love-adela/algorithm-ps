numbers = [] # [7, 8, 10, 13, 15, 19, 20, 23, 25]
for _ in range(9):
    numbers.append(int(input()))
summation = sum(numbers)

for i in range(len(numbers)):
    is_hundred = False
    for j in range(1, (len(numbers))):
        if i == j:
            continue
        if summation - (numbers[i] + numbers[j]) == 100:
            is_hundred = True
            for k in range(9):
                if k != i and k != j:
                    print(numbers[k])
    if is_hundred == True:
        break 
