# Bruteforce
from itertools import permutations
N, K = map(int, input().split())
kit = list(map(int, input().split()))
kit_dict = {}
for i in range(N):
    kit_dict[i+1] = kit[i]

def is_satisfied(w)->bool:
    if w >= 500: 
        return True
    return False

def check(kit_dict:dict, seq:tuple)->bool:
    weight = 500
    for i in seq:
        weight += kit_dict[i]
        weight -= K
        if not is_satisfied(weight):
            return False
    return True

def get_permutations():
    return list(permutations([param for param in range(1, N+1)]))

permutations = get_permutations()
cnt = 0
for i in range(len(permutations)):
    if check(kit_dict, permutations[i]):
        cnt += 1
print(cnt)
