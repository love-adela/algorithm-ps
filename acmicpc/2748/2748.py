first, second = 0, 1

for i in range(int(input())):
    first, second = first + second, first
print(first)