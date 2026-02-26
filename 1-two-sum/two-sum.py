class Solution(object):
    def twoSum(self, nums, target):
        seen = {}

        for i in range(len(nums)):
            current = nums[i]
            need = target - current

            if need in seen:
                return [seen[need], i]

            seen[current] = i