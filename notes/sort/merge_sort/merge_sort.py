def merge(list1, list2):
    merged_list = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
        
    # 남은 원소가 있는지 확인할 수도 있고
    # if i < len(list1):
    #     while i < len(list1):
    #         merged_list.append(list1[i])
    #         i += 1

    # if j < len(list2):
    #     while j < len(list2):
    #         merged_list.append(list2[j])
    #         j += 1
    # 확인하지 않을 수도 있다.
    merged_list += list1[i:]
    merged_list += list2[j:]
    return merged_list

# print(merge([1, 3, 5], [2, 4, 6]))
# assert merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]

def merge_sort(my_list):
    if len(my_list) < 2:
        return my_list

    left = my_list[:len(my_list) // 2]
    right = my_list[len(my_list) // 2:]   
    return merge(merge_sort(left), merge_sort(right))
some_list = [11, 3, 6, 4, 12, 1, 2]
print(merge_sort(some_list))
