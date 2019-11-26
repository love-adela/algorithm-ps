def is_prime(n:int)->bool:
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

a, b = int(input()), int(input())
prime = []
for i in range(a, b+1):
    while is_prime(i):
        prime.append(i)
        break

if sum(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(prime[0])
