"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the
sorted order, not the kth distinct element.
"""
import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
            :type nums: List[int]
            :type k: int
            :rtype: int
            """
        
        if nums:
            topk = nums[:k]
            heapq.heapify(topk)
            
            for num in nums[k:]:
                if num > topk[0]:
                    heapq.heappop(topk)
                    heapq.heappush(topk,num)
            
            return topk[0]


