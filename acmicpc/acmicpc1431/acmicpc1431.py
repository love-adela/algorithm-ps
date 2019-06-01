def sum_numbers(strings:str)->int:
    return sum([int(x) for x in strings if x.isdigit()])
    
def compare_strings(a:str, b:str)->bool: 
    length_of_a, length_of_b = len(a), len(b)
    sum_of_a, sum_of_b = sum_numbers(a), sum_numbers(b)

    if length_of_a != length_of_b:
        # 두 문자열 길이가 다를 때
        return length_of_a < length_of_b
    else:
        # 두 문자열 길이가 같을 때
        if sum_of_a != sum_of_b:
            return sum_of_a < sum_of_b
        else:
            return a < b

n = int(input())
unsorted = []

while n:
    unsorted.append(input())
    n -= 1

def sort(lst:list)->list:
    length = len(lst) 
    if length <= 1:
        return lst

    pivot = lst[-1]  
    left, right = [], []

    for i in range(0, length - 1):
        if compare_strings(lst[i], pivot) == True: 
            left.append(lst[i])
        else:
            right.append(lst[i])
    
    return sort(left) + [pivot] + sort(right)
print('\n'.join(sort(unsorted)))
