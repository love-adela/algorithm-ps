import sys
n = int(sys.stdin.readline())
number_dict = {}

# numbers = sys.stdin.read().splitlines()

for _ in range(n):
    number  = int(sys.stdin.readline())

    if number in number_dict:
        number_dict[number] += 1
    else:
        number_dict[number] = 1

for sorted in sorted(number_dict.items()):
    for i in range(sorted[1]):
        print(sorted[0])


