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

    def twoSum2(self, nums, target):
        hash_table = {}
        for i, num in enumerate(nums):
            if target - num in hash_table:
                print(hash_table)
                print(target - num)
                return [hash_table[target - num], i]
                break
            hash_table[num] = i
        return []

sol = Solution()
print(sol.twoSum([1, 3, 5, 6], 8))
print(sol.twoSum1([1, 3, 5, 6], 8))
print(sol.twoSum2([1, 3, 5, 6], 8))
