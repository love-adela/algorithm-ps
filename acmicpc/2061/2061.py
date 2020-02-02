import sys
k, l = map(int,sys.stdin.readline().split())

#def get_minimum_prime_factors(n):
#    for i in range(2, int(n**0.5)+1):
#        if n % i == 0:
#            return i

def eratosthenes(n:int):
    MAX = 1000000
    check = [0] * (MAX+1)
    check[0] = check[1] = True

    for i in range(2, MAX+1):
        if not check[i]:
            j = 2*i
            while j <= MAX:
                check[j] = True
                j += i
    sieve = []
    for i in range(n+1):
        if check[i] == False:
            sieve.append(i)
    return sieve

factors = eratosthenes(k)
if k % l == 0:
    if l < (k//l):
        print('GOOD')
    else:
        print(f'BAD {factors}')
else:
    print(f'BAD {factors}')
