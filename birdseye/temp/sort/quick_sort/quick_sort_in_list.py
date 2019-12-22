def quick_sort_in_list(unsorted_list, start, end):
    if end - start <= 0:
        return
    pivot = unsorted_list[end]
    i = start
    for j in range(start, end):
        if unsorted_list[j] <= pivot:
            unsorted_list[i], unsorted_list[j] = unsorted_list[j], unsorted_list[i]
            i += 1
    unsorted_list[i], unsorted_list[end] = unsorted_list[end], unsorted_list[i]
    
    quick_sort_in_list(unsorted_list, start, i - 1)
    quick_sort_in_list(unsorted_list, i + 1, end)

def quick_sort(a):
    quick_sort_in_list(a, 0, len(a) - 1)

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
quick_sort(d)
print(d)