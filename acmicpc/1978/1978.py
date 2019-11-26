# TODO: Sieve of Eratosthenes를 활용해서 미리 충분히 큰 수에 대해서는 채를 돌아서 미리 소수를 다 구해놓고 거기 있는지 확인해보자.

def is_prime(n:int)->bool:
    if n != 1:
        for i in range(2, n):
            if n % i == 0:
                return False
    else:
        return False
    return True

N = int(input())
numbers = list(map(int, input().split(' ')))
count = 0
for i in range(N):
    while is_prime(numbers[i]):
        count += 1
        break
print(count)
