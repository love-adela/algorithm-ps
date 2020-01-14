def is_prime(n:int)->bool:
    if n < 2:
        return False
    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True

def is_prime_half(n:int)->bool:
    if n < 2:
        return False
    for i in range(2, 2//n+1):
        if n % i == 0:
            return False
    return True

def is_prime_sqrt(n:int)->bool:
    if n < 2:
        return False
    for i in range(2, n**(1//2)+1):
        if n % i == 0:
            return False
    return True

def eratosthenes(a, b)->int:
    MAX = 1000000
    check = [0] * (MAX+1)
    check[0] = check[1] = True

    for i in range(2, MAX+1):
        if not check[i]:
            j = 2*i 
            while j <= MAX:
                check[j] = True
                j += i 

    for i in range(a, b+1):
        if check[i] == False:
            print(i)

eratosthenes(3, 16)



#for i in range(100):
#    print(f'{i}: {is_prime(i)}')
#    print(f'{i}: {is_prime_half(i)}')
#    print(f'{i}: {is_prime_sqrt(i)}')
