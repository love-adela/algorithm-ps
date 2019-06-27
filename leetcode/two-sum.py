class Solution:
    def twoSum(self, nums, target):
        keys = {}
        for i in range(len(nums)):
            if target - nums[i] in keys:
                return [keys[target - nums[i]], i]
            if nums[i] not in keys:
                keys[nums[i]] = i

    def twoSum1(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


sol = Solution()
print(sol.twoSum([1, 3, 5, 6], 8))
