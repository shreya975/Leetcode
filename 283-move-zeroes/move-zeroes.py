class Solution:
    def moveZeroes(self, nums):
        k = 0  # position to place next non-zero

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1

        # fill remaining with zeros
        for i in range(k, len(nums)):
            nums[i] = 0