"""
    Given an array of non-negative integers, you are initially positioned at the first index of the array.
    
    Each element in the array represents your maximum jump length at that position.
    
    Determine if you are able to reach the last index.
    https://leetcode.com/problems/jump-game/
    """
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        indexOfZero = []
        
        for i,x in enumerate(nums[:len(nums)-1]):
            if x == 0:
                indexOfZero.append(i)
    
        for index in indexOfZero:
            crossed = False
            for i,x in enumerate(nums[0:index]):
                print(x > index - i)
                if x > index - i:
                    crossed = True
            if not crossed:
                return False

                    return True
