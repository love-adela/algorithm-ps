# Using Loop
def binary_search(elem, sorted_list):
    start = 0
    end = len(sorted_list) -1 

    while start <= end:
        midpoint = (start + end) // 2
        if elem == sorted_list[midpoint]:
            return midpoint
        elif elem < sorted_list[midpoint]:
            end = midpoint - 1
        else:
            start = midpoint + 1

    return None

# Using Recursive 
def binary_recursive_search(element, sorted_list, start_index=0, end_index=None)->int:
    if end_index is None:
        end_index = len(sorted_list) - 1
    if start_index > end_index:
        return None
    
    midpoint = (start_index + end_index) // 2
    if element == sorted_list[midpoint]:
        return midpoint
    elif element < sorted_list[midpoint]:
        return binary_recursive_search(element, sorted_list, start_index, midpoint-1)
    return binary_recursive_search(element, sorted_list, midpoint+1, end_index)

# Test

print(binary_search(2, [2, 3, 5, 7, 11])) # 0
print(binary_search(0, [2, 3, 5, 7, 11])) # None
print(binary_search(5, [2, 3, 5, 7, 11])) # 2
print(binary_search(3, [2, 3, 5, 7, 11])) # 1
print(binary_search(11, [2, 3, 5, 7, 11])) # 4
print(binary_recursive_search(2, [2, 3, 5, 7, 11])) # 0
print(binary_recursive_search(0, [2, 3, 5, 7, 11])) # None
print(binary_recursive_search(5, [2, 3, 5, 7, 11])) # 2
print(binary_recursive_search(3, [2, 3, 5, 7, 11])) # 1
print(binary_recursive_search(11, [2, 3, 5, 7, 11])) # 4
