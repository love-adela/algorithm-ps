for i in range(1000, 10000):
    num, sixteen = i, 0
    while num is not 0:
        sixteen += num % 16
        num //= 16
    num, twelve = i, 0
    while num is not 0:
        twelve += num % 12
        num //= 12
    num, ten = i, 0
    while num is not 0:
        ten += num % 10
        num //= 10
    if sixteen == twelve == ten:
        print(i)
