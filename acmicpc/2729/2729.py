n = int(input())
for i in range(n):
    a, b = input().split()
    a = '0b' + a
    b = '0b' + b
    decimal = int(a, 2) + int(b, 2)
    print(bin(decimal)[2:])
