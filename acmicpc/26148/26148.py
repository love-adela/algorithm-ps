n = int(input())
print(30 if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0 else 29)
