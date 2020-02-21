"""
    https://leetcode.com/problems/house-robber-ii/
    You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
    
    Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
    """
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(nums):
            if len(nums) > 0:
                total = [0,nums[0]]
                for i in range(1,len(nums)):
                    total.append(max(total[-1],total[-2]+nums[i]))
                return total[-1]
            return 0
        
        if len(nums) > 3:
            return max(helper(nums[:len(nums)-1]), helper(nums[1:]))
        elif nums:
            return max(nums)
        return 0
