while True:
    t = int(input())
    if t == 0:
        break
    total = 0
    for i in range(1, t+1):
        total += i**2
    print(total)
