def jewrly(N):
    for i in range(len(list_a)):
        iteration = 0
        for iteration in range(len(list_a) - (1 + i)):
            if list_a[iteration] > list_a[iteration + 1]:
                list_a[iteration], list_a[iteration + 1] = list_a[iteration + 1], list_a[iteration]

    for i in range(len(list_b)):
        iteration = 0
        for iteration in range(len(list_b) - (1 + i)):
            if list_b[iteration] < list_b[iteration +1]:
                list_b[iteration], list_b[iteration + 1] = list_b[iteration + 1], list_b[iteration]

    sum = 0
    for i in range(len(list_a)):
        multiplied_value = list_a[i] * list_b[i]
        sum += multiplied_value
        
    return sum

example = int(input())
list_a = [int(param) for param in input().split(' ')]
list_b = [int(param) for param in input().split(' ')]

for i in range(0, example):
    answer = jewrly(i)
print(answer)