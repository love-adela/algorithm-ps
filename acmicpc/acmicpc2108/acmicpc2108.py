import sys
from collections import Counter

N = int(sys.stdin.readline())
numbers = [int(param) for param in sys.stdin.readlines()]

def mean(nums:list)->int:
    return round(sum(nums)/len(nums))

def median(nums:list):
    nums.sort()
    mid = nums[len(nums)//2]
    return mid

def mode(nums:list):
    mode_dict = Counter(nums)
    modes = mode_dict.most_common()
    if len(nums) > 1:
        if modes[0][1] == modes[1][1]:
            mod = modes[1][0]
        else:
            mod = modes[0][0]
    else:
        mod = modes[0][0]
    return mod

def numbers_range(nums:list):
    nums.sort()
    minimum = min(nums)
    maximum = max(nums)
    return abs(maximum-minimum)
    

print(mean(numbers))
print(median(numbers))
print(mode(numbers))
print(numbers_range(numbers))
