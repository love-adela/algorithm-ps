while True:
    n, q = map(int, input().split())
    if (n,q) == (0,0):
        break
    candidates = [0] * 101
    for _ in range(n):
        temp = [int(param) for param in input().split()][1:]
        for item in temp:
            candidates[item] += 1
    if max(candidates) < q:
        print(0)
    else:
        print(candidates.index(max(candidates)))

