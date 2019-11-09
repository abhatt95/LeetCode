"""
Given an array of integers, return indices of the
 two numbers such that they add up to a specific target.

You may assume that each input would have exactly one
 solution, and you may not use the same element twice.
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = set(nums)
        for i,x in enumerate(nums):
            if target-x in lookup:
                if nums.index(target-x) != i:
                    return sorted([i,nums.index(target-x)])
                
        