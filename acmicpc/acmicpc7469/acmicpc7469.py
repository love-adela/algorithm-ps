# 입력받은 리스트 a를 오름차순으로 정렬할 것
# a[i] < value < a[j]를 범위를 가진 새 리스트 b로 슬라이싱할 것
# 리스트 b의 b[k]를 리턴시킬 것

def Q(i, j, k):
    length_of_list, number_of_call = input().split(' ')
    input_list = [int(param) for param in input().split(' ')].sort()    
    new_list = input_list[i - 1:] + input_list[:j - 1]

    for _ in range(number_of_call):
        i, j, k = input().split(' ')
        new_list[i]
    return new_list[k]
    
 