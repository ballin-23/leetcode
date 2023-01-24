class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero_counter = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_counter += 1
        for i in range(zero_counter):
            nums.remove(0)
            nums.append(0)