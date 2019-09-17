def binary_recursive_search(element, some_list, start_index=0, end_index=None)->int:
    if end_index is None:
        end_index = len(some_list) -1
    if start_index > end_index:
        return None 

    midpoint = (start_index + end_index) // 2
    if element == some_list[midpoint]:
        return midpoint
    elif element < some_list[midpoint]:
        return binary_recursive_search(element, some_list, start_index, midpoint-1)
    return binary_recursive_search(element, some_list, midpoint+1, end_index)

print(binary_recursive_search(2, [2, 3, 5, 7, 11]))
print(binary_recursive_search(0, [2, 3, 5, 7, 11]))
print(binary_recursive_search(5, [2, 3, 5, 7, 11]))
print(binary_recursive_search(3, [2, 3, 5, 7, 11]))
print(binary_recursive_search(11, [2, 3, 5, 7, 11]))
