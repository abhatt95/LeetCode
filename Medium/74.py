"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix:
            if len(matrix) == 1:
                for x in matrix[0]:
                    if x == target:
                        return True
            if matrix[0]:
                i = 0
                while i < len(matrix):
                    if target == matrix[i][0]:
                        return True
                    if target>matrix[i][0]:
                        i += 1
                    else:
                        break
                if i>0 :
                    for x in matrix[i-1]:
                        if x == target:
                            return True
        
            
        return False
                
        
        