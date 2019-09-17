import sys
# quick sort (nlogn)
def quick_sort_list(unordered:list, start:int, end:int):
    if end - start <= 0:
        return 
    pivot = unordered[end]
    i = start
    for j in range(start, end):
        if unordered[j] <= pivot:
            unordered[i], unordered[j] = unordered[j], unordered[i]
            i += 1
    unordered[i], unordered[end] = unordered[end], unordered[i]

    quick_sort_list(unordered, start, i-1)
    quick_sort_list(unordered, i+1, end)

def quick_sort(a):
    quick_sort_list(a, 0, len(a)-1)


num_list = list(map(int, sys.stdin.read().splitlines()[1:]))
quick_sort(num_list)
sys.stdout.write('\n'.join(str(num) for num in num_list)+'\n')
