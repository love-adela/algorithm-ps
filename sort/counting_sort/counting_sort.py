# Time Complexity : O(n)
# 요소 값을 명시적으로 비교하지 않아도 정렬할 수 있다.
# input_list의 max_value에 따라서 for 문을 도는 횟수가 달라짐에 따라 비효율적일 수 있다.
# max_value가 counting sort의 복잡성을 지배한다.
# stable sort

def counting_sort(input_list, max_value):
    result_list = [-1] * len(input_list)
    counting_list = [0] * (max_value + 1)

    for elem in input_list:
        counting_list[elem] += 1

    for i in range(max_value):
        counting_list[i + 1] += counting_list[i]

    for j in reversed(range(len(input_list))):
    	result_list[counting_list[input_list[j]] - 1] = input_list[j]
    	counting_list[input_list[j]] -= 1

    return result_list

unordered_list = [95, 1, 656, 72, 35, 83, 760, 944, 876, 684, 767, 709]
print(counting_sort(unordered_list, max(unordered_list)))