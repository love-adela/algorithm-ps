import math

def gcd(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i

gcd_list = []
while True:
    prompt = input("입력하셈")
    if prompt == "":
        break
    gcd_list = [int(i) for i in prompt.split()]
    a, b = gcd_list # unpack

    print(gcd(a, b))
    print(math.gcd(a, b))
