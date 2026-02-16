class Solution:
    def moveZeroes(self, nums):
        insert_pos = 0

        # Step 1: move all non-zero elements forward
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos] = nums[i]
                insert_pos += 1

        # Step 2: fill remaining positions with 0
        for i in range(insert_pos, len(nums)):
            nums[i] = 0
