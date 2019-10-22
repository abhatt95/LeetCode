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
        
        profit_lookup = {}
        def get_max_profit(root):
            
            if root == None:
                return 0
            
            if root.left == None and root.right == None:
                return root.val
            
            left_left_profit =  left_right_profit = right_left_profit = right_right_profit = 0
            
            if root.left != None:
                if root.left.left not in profit_lookup:
                    profit_lookup[root.left.left] = get_max_profit(root.left.left)
                left_left_profit = profit_lookup[root.left.left]
                if root.left.right not in profit_lookup:
                    profit_lookup[root.left.right] = get_max_profit(root.left.right)
                left_right_profit = profit_lookup[root.left.right]
                
            if root.right != None:
                if root.right.left not in profit_lookup:
                    profit_lookup[root.right.left] = get_max_profit(root.right.left)
                right_left_profit = profit_lookup[root.right.left]
                if root.right.right not in profit_lookup:
                    profit_lookup[root.right.right] = get_max_profit(root.right.right)
                right_right_profit = profit_lookup[root.right.right]
                
            return max(root.val+left_left_profit+left_right_profit+right_left_profit+right_right_profit,get_max_profit(root.left) + get_max_profit(root.right) )
        return get_max_profit(root)
        