def get_divisor(k):
    divisors = []
    for i in range(1, k):
        if k % i == 0:
            divisors.append(i)
    return divisors
    
while True:
    n = int(input())
    if n == -1:
        break
    divisors = get_divisor(n)
    if n == sum(divisors):
        print(f'{n}', end=' = ')
        print(' + '.join(list(map(str, divisors))))
    elif n != sum(divisors):
        print(f'{n} is NOT perfect.')
