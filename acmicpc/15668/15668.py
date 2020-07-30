N = int(input())
length = len(str(N))

max_v = min(N // 2, int('9'*(11-length))//10)

def is_valid(a, b):
    s = str(a) + str(b)
    set1 = set()
    for c in s:
        set1.add(c)
    return len(set1) == len(s)

flag = False

for i in range(1, max_v+1):
    if is_valid(i, N-i):
        flag = True
        break

if flag:
    print(f'{i} + {N-i}')
else:
    print(-1)
