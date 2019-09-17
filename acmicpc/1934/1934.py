def find_lcm(a:int, b:int)->int:
    
    if a <= b: # 1 45000
        for i in range(1, a + 1):
            if a % i == 0 and b % i == 0:
                gcd = i
                lcm = int(a * b / gcd)
        return lcm

    if a > b: # 6, 2
        for i in range(1, b + 1): 
            if a % i == 0 and b % i == 0:
                gcd = i
                lcm = int(a * b / gcd)
        return lcm

n = int(input())
for _ in range(n):
    nums = [int(i) for i in input().split()]
    a, b = nums
    print(find_lcm(a, b))

