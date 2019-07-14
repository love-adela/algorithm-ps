a = int(input())
b = input()

one = a * int(b[2])
ten = a * int(b[1])
hundread = a * int(b[0])
print(f'{one}\n{ten}\n{hundread}')
print(one + ten * 10 + hundread * 100)
