def plus_minus(arr):
    n = len(arr)

    p_sum = 0
    n_sum = 0
    z_sum = 0

    p_answer = 0
    n_answer = 0
    z_answer = 0

    for i in range(0, n):
        if arr[i] > 0:
            p_sum += 1
        elif arr[i] < 0:
            n_sum += 1
        else:
            z_sum +=1

    p_answer = p_sum / n
    n_answer = n_sum / n
    z_answer = z_sum / n

    print(p_answer)
    print(n_answer)
    print(z_answer)

n = 6
arr = [-4, 3, -9, 0, 4, 1]

print(plus_minus(arr))