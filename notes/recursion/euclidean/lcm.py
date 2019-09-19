# Python 내장함수에는 GCD를 구할 수 있는 최대공약수는 있지만, LCD를 구할 수 있는 최소공배수는 없다.


def lcm(a, b):
    if a <= b:
        for i in range(1, a):
            if a % i == 0 and b % i == 0:
                gcd = i
                lcm = int(a * b / gcd)
        return lcm

    if a > b:
        for i in range(1, b):
            if a % i == 0 and b % i == 0:
                gcd = i
                lcm = int(a * b / gcd)
        return lcm


lcm_list = []
while True:
    input_integer = input("입력하세여")
    if input_integer == "":
        break
    lcm_list = [int(i) for i in input_integer.split()]
    print(lcm_list)

    a, b = lcm_list
    print(lcm(a, b))
