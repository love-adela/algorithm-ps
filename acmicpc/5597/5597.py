cnt = 0
numbers = []
while True:
    numbers.append(int(input()))
    cnt += 1
    if cnt == 28:
        break

for i in range(30):
    if i + 1 not in sorted(numbers):
        print(i+1)


