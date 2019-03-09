import math


def gcd(a, b):
    if a >= b:
        for i in range(1, a): # O(a)
            if a % i == 0 and b % i == 0:
                gcd = i
        return gcd
    if b > a:
        for i in range(1, b): # O(b)
            if a % i == 0 and b % i == 0:
                gcd = i
        return gcd

# print(type(line.split()))
# print(repr(line.split()))


gcd_list = []
while True:
    prompt = input("입력하셈")
    if prompt == "":
        break
    gcd_list = [int(i) for i in prompt.split()]
    a, b = gcd_list # unpack

    print(gcd(a, b))
    print(math.gcd(a, b))
