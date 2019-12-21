from itertools import permutations

N = int(input())
params = tuple(input().split())

def is_matched(iterator):
    params_list = sorted(list(permutations(iterator)))
    for i in range(len(params_list)):
        if params_list[i] == params:
            return True
#            if params_list[-1] == params:
#                print(-1)
#                break
        else:
            return False
#                print(' '.join(params_list[i+1]))
#                break

if is_matched(params) is True:
    print(' '.join(params
else:
    print(-1)



