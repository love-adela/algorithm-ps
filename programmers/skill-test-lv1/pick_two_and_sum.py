# https://programmers.co.kr/learn/courses/30/lessons/68644
def solution(num:list)->list:
    answer = set()
    for i in range(len(num)):
        for j in range(len(num)):
            if i != j:
                answer.add(num[i] + num[j])
    return sorted(list(map(int, answer)))

# Test
# numbers = [2,1,3,4,1] # result = [2,3,4,5,6,7]
numbers = [5,0,2,7] # result = [2,5,7,9,12]
# numbers = [3, 2, 1]
print(solution(numbers))
