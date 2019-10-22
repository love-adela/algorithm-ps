class Solution:
    def moveZeroes(self, nums: list) -> None:
        for items in nums:
            if items == 0:
                nums.append(nums.pop(nums.index(0)))
