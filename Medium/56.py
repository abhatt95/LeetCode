"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
https://leetcode.com/problems/merge-intervals/
"""
from heapq import heappush,heappop,heapify

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        if not intervals:
            return intervals
        
        heapify(intervals)
        
        merged_intervals = []
        
        while len(intervals) > 1:
            first,second = heappop(intervals),heappop(intervals)
            
            if first[0] <= second[0] <= first[1]:
                merged = [0,0]
                merged[0],merged[1] = min(first+second),max(first+second)
                
                if intervals:
                    heappush(intervals,merged)
                else:
                    merged_intervals.append(merged)
            else:
                merged_intervals.append(first)
                heappush(intervals,second)
        if intervals:
            merged_intervals.append(intervals[0])
        return merged_intervals
                
        