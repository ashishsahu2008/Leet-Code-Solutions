'''
https://leetcode.com/problems/move-zeroes/description/

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_pointer = self.findNextZero(0, nums)
        if zero_pointer is None:
            return
        for i in range(len(nums)):
            if nums[i] != 0 and zero_pointer < i:
                x = nums[i]
                nums[i] = nums[zero_pointer]
                nums[zero_pointer] = x
                zero_pointer = self.findNextZero(zero_pointer+1, nums)
                if zero_pointer is None:
                    return
    def findNextZero(self, start, nums):
        for y in range(start, len(nums)):
            if nums[y] == 0:
                return y
