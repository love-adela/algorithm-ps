import sys
N = int(sys.stdin.readline())
numbers = [0] * 10001

for _ in range(N):
    numbers[int(sys.stdin.readline())] += 1
for num in range(len(numbers)):
    if numbers[num] != 0:
        print(f"{num}\n"*numbers[num], end="")
