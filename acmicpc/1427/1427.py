number_list = [param for param in input()]

# Insertion Sort

def sort(digits:list)-> list:
    sorted_list = []
    for digit in digits:
        # 2 1 4 3
        i = 0 
        while i < len(sorted_list) and digit <= sorted_list[i]:
            i += 1
        sorted_list.insert(i, digit)
    return sorted_list

print(''.join(sort(number_list)))

