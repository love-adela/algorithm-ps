A, B, N, M = map(int, input().split())
count = 0
while M:
    count += 1
    if A < B:
        if M % B != 0:
            M -= A
            continue
        else:
            M //= B
            continue
print(count)
    
