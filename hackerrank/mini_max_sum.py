def mini_max_sum(arr):

    n = len(arr)
    arr.sort()
    min_sum = 0
    max_sum = 0

    max_sum += sum(arr[1:])
    min_sum += sum(arr[:n-1])

#    print((map(str, max_sum)).join(" "), min_sum)
    print(max_sum, " ", min_sum)

arr = [3, 1, 4, 2, 5]
print(mini_max_sum(arr))
