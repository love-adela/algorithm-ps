n = int(input())
if n % 8 == 1:
    print(1)
if n % 8 == 0:
    print(2)
elif n % 8 == 2:
    print(2)
elif n % 4 == 3:
    print(3)
elif n % 4 == 0:
    print(4)
elif n % 4 == 2:
    print(4)
elif n % 8 == 5:
    print(5)
