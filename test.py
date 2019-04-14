def merge(list1, list2):
    merged_list = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        merged_list.append(list2[j])
        j += 1

    merged_list += list1[i:]
    merged_list += list2[j:]
    return merged_list


def merge_sort(my_list):
    if len(my_list) < 2:
        return my_list
    left = my_list[:len(my_list) // 2]
    right = my_list[len(my_list) // 2:]
    return merge(merge_sort(left), merge_sort(right))
some_list = [11, 3, 6, 4, 12, 1, 2]
print(merge_sort(some_list))

