n = int(input())
cars = map(int, input().split())
count = 0
for car in cars:
    if car == n:
        count += 1
print(count)
