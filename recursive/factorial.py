# n = int(input("입력하세여"))
import math

def factorial(n):
    if n == 1:
        return 1
    return factorial(n-1) * n
print(factorial(10))

print(math.factorial(10))

# O(n)
# n * (n -1) * (n-2) * (n-3)


