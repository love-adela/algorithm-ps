def is_hansu(num)->bool:
    nums = list(map(int, num))
    if len(num) != 1 and len(num) != 2:
        for i in range(1, len(num)-1):
            if nums[1] - nums[2] == nums[0] - nums[1]:
                pass
            else:
                return False
    return True

N = input()
count = 0
for i in range(1, int(N)+1):
    if is_hansu(str(i)):
        count += 1
print(count)
