"""
    Given the root of a binary search tree with distinct values, modify it so that every node has a new value equal to the sum of the values of the original tree that are greater than or equal to node.val.
    
    As a reminder, a binary search tree is a tree that satisfies these constraints:
    
    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.
    """
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import bisect

class Solution(object):
    def bstToGst(self, root):
        """
            :type root: TreeNode
            :rtype: TreeNode
            """
        
        order = []
        lookup = {}
        
        def inorder(opt,root):
            if root:
                inorder(opt,root.left)
                if opt:
                    order.append(root.val)
                else:
                    root.val = lookup[root.val]
                inorder(opt,root.right)
    
        inorder(True,root)
        
        s = 0
        for num in order[::-1]:
            lookup[num] = s + num
            s += num

                inorder(False,root)

return root
