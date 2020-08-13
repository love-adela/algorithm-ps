N = int(input())
lst = list(input())
for _ in range(N-1):
    lst_for_comparison = list(input())
    for i in range(len(lst)):
        if lst[i] != lst_for_comparison[i]:
            lst[i] = '?'
print(''.join(lst))
