A, B = input().split()

len_a, len_b = len(A), len(B)
index_a, index_b = 0, 0
flag = False

for i in range(len_a):
    for j in range(len_b):
        if A[i] == B[j]:
            index_a, index_b = i, j
            flag = True
            break
    if flag: break

for j in range(len_b):
    for i in range(len_a):
        if j == index_b:
            print(A[i], end='')
        elif i == index_a:
            print(B[j], end='')
        else:
            print('.', end='')
    print()
