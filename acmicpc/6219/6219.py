A, B, D = map(int, input().split())

def eratosthenes(m, n, k):
    MAX = 4000000
    check = [0] * (MAX+1)
    check[0] = check[1] = True
    count = 0

    for i in range(2, MAX+1):
        if not check[i]:
            j = 2*i
            while j < MAX:
                check[j] = True
                j += i
    k = str(k)
    for i in range(m, n+1):
        if check[i] == False:
            if k in str(i):
                count += 1
    print(count)
    
eratosthenes(A, B, D)
