"""
    A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
    
    The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
    
    How many possible unique paths are there?
    """

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        if m == 1 and n == 1:
            return 1
        
        table = [[ 1 for i in range(m) ] for j in range(n)]
        table[0][0] = 0
        
        for j in range (1, m):
            for i in range(1, n):
                table[i][j] = table[i-1][j] + table[i][j-1]

    return table[-1][-1]
