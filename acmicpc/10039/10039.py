nums = [int(input()) for _ in range(5)]
for i in range(len(nums)):
    if nums[i] < 40:
        nums[i] = 40
print(sum(nums)//5)


