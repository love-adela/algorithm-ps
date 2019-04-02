numbers = [int(param) for param in input().split(' ')]

# insertion sort - 두 배열을 활용하는 방법 # 첫번째
list = []
for i in range(len(numbers)):
    is_inserted = False
    for j in range(len(list)):
        if numbers[i] < list[j]:
            is_inserted = True
            list.insert(j, numbers[i])
            break
    if not is_inserted:
        list.append(numbers[i])
print(' '.join(str(num) for num in list))

# insertion sort - 두 배열을 활용하는 방법 # 두번째
sorted = []
for number in numbers:
    not_inserted = True
    for i in range(len(sorted)):
        if number < sorted[i]:
            not_inserted = False
            sorted.insert(i, number)
            break
    if not_inserted:
        sorted.append(number)

print(sorted)

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

# Codeit 풀이
def insertion_sort(my_list):
    for index in range(1, len(my_list)):
        key = my_list[index]    
        position = index
        while position > 0 and my_list[position - 1] > key:
            print(f"Swapped {my_list[position]} for {my_list[position - 1]}")
            my_list[position] = my_list[position - 1]
            print(my_list)
            position -= 1
        
        my_list[position] = key
    return my_list

def insertion_sort_2(my_list):
    for i in range(len(my_list)):
        key = my_list[i]

        j = i - 1
        while j >= 0 and my_list[j] > key:
            my_list[j + 1] = my_list[j]
            j = j - 1

        my_list[j + 1] = key


some_list = [11, 3, 6, 4, 12, 1, 2]
insertion_sort(some_list)
insertion_sort_2(some_list)
print(some_list)