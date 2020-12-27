import random

class Solution:
    def binarySearch(self, nums, target):
        
        left = 0
        right = len(nums)-1
        
        while left <= right:
            mid = left + (right-left)//2
            if target == nums[mid]:
                return mid
            if nums[mid] > target:
                right = mid - 1
            if nums[mid] < target :
                left = mid + 1
                
        return -1

inputs = [[-100,-50,-10,0,11,15,20,30]]

for input in inputs:
    s = Solution()
    num = random.choice(input)
    print(num,s.binarySearch(input,num))
    