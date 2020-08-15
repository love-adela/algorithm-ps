# 정답비율 = (문제를 맞은 사람의 수) / (문제를 맞은 사람의 수 + (문제를 맞은 각 사람이 그 문제를 맞기 전까지 틀린 횟수의 총 합)) × 100
import sys
from collections import defaultdict
N = int(sys.stdin.readline())
user_dict = defaultdict(list)

"""
1. N개의 정보 중 같은 사용자가 제출한 결과를 묶는다
2. 각 사용자의 제출결과에 '맞았습니다'가 있는지 알아본다.
3. 관리자가 제출한건 맞은 결과, 틀린 결과에 포함시키지 않는다.
4. 전체 사용자 중 맞은 사람의 수를 구한다.
5. 전체 사용자의 맞기 전까지 틀린 횟수를 구한다.
"""
for _ in range(N):
    _, user_id, result, _, _, _, _ = sys.stdin.readline().split()
    user_dict[user_id].append(result)

def is_answerer(results:list)->bool:
    if '4' not in results:
        return False
    return True

def get_number_of_wrong_results(results:list)->int:
    return results.index('4')

def is_admin(user:str)->bool:
    if user == 'megalusion':
        return True
    return False

count_answerer, count_wrong = 0, 0
for user in user_dict: # {'megalusion':[4, 4, 4], 'a': [6, 7, 4]}
    each_results = user_dict[user] # [4, 4, 4]
    if is_answerer(each_results) and not is_admin(user):
        count_answerer += 1 
        count_wrong += get_number_of_wrong_results(each_results)
total = count_answerer + count_wrong
if total == 0:
    print(0)
else:
    print((count_answerer / total) * 100)
