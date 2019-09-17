import random

numbers = [i for i in range(1, 100)]
n = random.sample(numbers, 1)[0]
target = [i for i in range(1, 10000)]
k = random.sample(target, 1)[0]
value = [i for i in range(1, 100000)]
v = random.sample(value, 1)[0]

print(n, k)
for _ in range(n):
    print(v)
