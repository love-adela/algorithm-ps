from itertools import permutations

N = int(input())

params = tuple(input().split())
params_list = sorted(list(permutations(params)))
for i in range(len(params_list)):
    if params_list[i] == params:
        if params_list[-1] == params:
            print(-1)
            break
        else:
            print(' '.join(params_list[i+1]))
            break

