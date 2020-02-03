import sys
k, l = map(int,sys.stdin.readline().split())

def eratosthenes(n:int):
    MAX = 1000000
    is_prime = [True] * (MAX+1)
    is_prime[0] = is_prime[1] = True

    for i in range(2, MAX+1):
        if is_prime[i]:
            j = 2*i
        while j <= MAX:
            is_prime[j] = False
            j += i

    primes = []
    for i in range(2, len(is_prime)):
        if is_prime[i]:
            primes.append(i)
    return primes 

def main(primes:list):
    for elem in primes:
        if k % elem == 0: 
            if elem >= l:
                return 'GOOD'
            else:
                return f'BAD {elem}'

    return 'GOOD'
factors = eratosthenes(k)
print(main(factors))
