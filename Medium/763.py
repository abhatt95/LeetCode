"""
A string S of lowercase letters is given. 
We want to partition this string into as many 
parts as possible so that each letter appears 
in at most one part, and return a list of integers 
representing the size of these parts.
https://leetcode.com/problems/partition-labels/
"""

from collections import defaultdict

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
                    
        lookup = defaultdict(int)

        for i,c in enumerate(S):
            lookup[c] = max(lookup.get(c,0),i)

        output = []
        
        start = 0 
        expected_end = end = lookup[S[start]]
        
        while start < len(S):
            for i in range(start,end):
                if lookup[S[i]] > end:
                    end = lookup[S[i]]
                    break
            if end == expected_end:
                output.append(end-start+1)
                start = end + 1
                if start < len(S):
                    expected_end = end = lookup[S[start]]
            else:
                expected_end = end 
                
        return output
 
                
        