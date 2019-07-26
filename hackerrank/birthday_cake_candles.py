def birthday_candles(ar):

    n = len(ar)
    max = -1
    count = 0

    for i in range(0, n):
        if ar[i] > max:
            max = ar[i]
            count = 0
            count += 1
        elif ar[i] == max:
            count += 1
    return count

n = 10
ar = [44, 53, 31, 27, 77, 60, 66, 77, 26, 36]

print(birthday_candles(ar))