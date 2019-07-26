def diagonal_difference(a):

    n = len(a)

    r_sum = 0
    l_sum = 0


    for i in range (0, n):
        r_sum = r_sum + a[i][i]
        l_sum = l_sum + a[i][n-1 -i]
    #return r_sum, l_sum

    min = r_sum - l_sum
    result = abs(min)
    return result



n = 3
a = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12],
    ]

print(diagonal_difference(a))