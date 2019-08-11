def quick_sort_in_list(unsorted:list, start, end)->list:
    if end - start <= 0:
        return
    pivot = unsorted[end]
    i = start

    for j in range(start, end):
        if unsorted[j] <= pivot:
            unsorted[i], unsorted[j] = unsorted[j], unsorted[i]
            i += 1
    unsorted[i], unsorted[end] = unsorted[end], unsorted[i]
    
    quick_sort_in_list(unsorted, start, i - 1)
    quick_sort_in_list(unsorted, i + 1, end)   


def quick_sort(a):
    quick_sort_in_list(a, 0, len(a) -1)

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
quick_sort(d)
print(d)
