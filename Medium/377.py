"""
    Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.
    """
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        lookup = {}
        
        def helper(current_total):
            if current_total < 0:
                return 0
            if current_total == 0:
                return 1
            currentWays = 0
            for n in nums:
                if current_total-n not in lookup:
                    lookup[current_total-n] = helper(current_total-n)
                currentWays +=  lookup[current_total-n]
            return currentWays
        return helper(target)


