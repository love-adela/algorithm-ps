t = int(input())
for _ in range(t):
    evens = [int(param) for param in input().split() if int(param) % 2 == 0]
    print(sum(evens), min(evens))

