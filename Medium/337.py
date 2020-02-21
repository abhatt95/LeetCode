"""
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        
        def sr(root):
            
            if not root: return (0,0)
            
            left,right = sr(root.left), sr(root.right)
            
            current = root.val + left[1] + right[1]
            
            later = max(left) + max(right)
            
            return (current,later)
        
        return max(sr(root))
