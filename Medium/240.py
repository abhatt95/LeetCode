"""
Write an efficient algorithm that searches for a 
value in an m x n matrix. This matrix has the 
following properties:

Integers in each row are sorted in ascending from 
left to right.Integers in each column are sorted 
in ascending from top to bottom.
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix:
            i,j = 0,len(matrix[0])-1
            row,col = len(matrix),0
            while i<row and j >=col:
                if matrix[i][j] == target:
                    return True
                if matrix[i][j] > target:
                    j -= 1
                else:
                    i += 1
        return False            