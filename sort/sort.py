# 5 12 23 34 45 54 56 234 345 3432
# 23 34 234 5 12 345 3432 45 54 56
numbers = [int(param) for param in input().split(' ')]

# selection sort - (1)
# for i in range(len(numbers)):
#     for j in range(i, len(numbers)):
#         if numbers[i] > numbers[j]:
#             numbers[i], numbers[j] = numbers[j], numbers[i]
# print(' '.join(str(num) for num in numbers))

# selection sort - (2)
# for i in range(len(numbers)):
#     min_index = i
#     for j in range(i + 1, len(numbers)):
#         value = numbers[j]
#         if value > numbers[min_index]:
#             min_index = j
#     numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

# bubble sort
# for i in range(len(numbers)):
#     iteration = 0
#     for iteration in range(len(numbers) - (1 + i)):
#         if numbers[iteration] > numbers[iteration + 1]:
#             numbers[iteration], numbers[iteration + 1] = numbers[iteration + 1], numbers[iteration]
# print(' '.join(str(num) for num in numbers))]

# insertion sort - 두 배열을 활용하는 방법 # 첫번째
# list = []
# for i in range(len(numbers)):
#     is_inserted = False
#     for j in range(len(list)):
#         if numbers[i] < list[j]:
#             is_inserted = True
#             list.insert(j, numbers[i])
#             break
#     if not is_inserted:
#         list.append(numbers[i])
# print(' '.join(str(num) for num in list))
#
# insertion sort - 두 배열을 활용하는 방법 # 두번째
# sorted = []
# for number in numbers:
#     not_inserted = True
#     for i in range(len(sorted)):
#         if number < sorted[i]:
#             not_inserted = False
#             sorted.insert(i, number)
#             break
#     if not_inserted:
#         sorted.append(number)
#
# print(sorted)


# insertion sort - 배열 하나로 정렬하는 방법

def delete(list, index):
    new_list = list.copy()

    for i in range(index, len(list) - 1):
        print(new_list)
        new_list[i] = new_list[i+1]
    new_list.pop()
    return new_list


def insert(list, index, new_element):
    new_list = list.copy()
    new_list.append(None)
    for i in range(index +1, len(list) - 1):
        print(new_list)
        new_list[i] = new_list[i+1]
        # new_list[index] = new_element
        # new_list += new_list[index]
    return new_list


result = insert(['a', 'b', 'c', 'd', 'e'], 1, 'f')
print(result)
# ['a', 'b', 'd', 'e']
#
# numbers = [1, 3, 5, 2, 4]
# # for i in range(len(numbers)):
# i = 3
# for j in range(len(numbers) - 1):
#     if numbers[j] > numbers[i]:
#         temp = numbers[i]
#         # del numbers[i]
#         # numbers.insert(j, temp)
#         break
#
# print(' '.join(str(num) for num in numbers))
