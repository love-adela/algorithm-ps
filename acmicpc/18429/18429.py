# Bruteforce
from itertools import permutations
N, K = map(int, input().split())
kit = list(map(int, input().split()))

def is_satisfied(w)->bool:
    if w >= 0: # weight가 0 이상인지만 확인
        return True
    return False

def check(seq:tuple)->bool:
    weight = 0
    for i in seq:
        weight += kit[i]
        weight -= K
        if not is_satisfied(weight):
            return False
    return True

def get_permutations(): #TODO: permutations 직접 구현하기
    return list(permutations([param for param in range(N)]))

permutations = get_permutations()
cnt = 0
for i in range(len(permutations)):
    if check(permutations[i]):
        cnt += 1
print(cnt)
