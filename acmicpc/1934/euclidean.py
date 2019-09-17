def euclidean(a:int, b:int)->int:
    if b == 0:
        return a
    return euclidean(b, a % b)

def find_lcm(a:int, b:int)->int:
    lcm = int(a * b / euclidean(a, b))
    return lcm

n = int(input())
for _ in range(n):
    nums = [int(i) for i in input().split()]
    a, b = nums
    print(find_lcm(a, b))
