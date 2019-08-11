n = int(input()) # 꽃의 개수

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
    
for i in range(n):
    input_date = list(map(int, input().split()))
    quick_sort(input_date)
    print(input_date)


def tuple():
    for i in range(n):
        blooming_date = () # (month, day)
        falling_date = ()
        # input_date = tuple(map(int, input().split())) # (1, 1, 5, 31)

        for j in range(len(date)//2):
            blooming_date += (input_date[j],)
        for j in range(2, 4):
            falling_date += (input_date[j],)

# 지는 날 기준으로 오름차순 정렬 (quick sort) : 피어있는 기간이 제일 긴 것을 먼저 정렬하면 중복이 최소화되지 않을까?


