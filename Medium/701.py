# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Given the root node of a binary search tree (BST) and a value 
to be inserted into the tree, insert the value into the BST. 
Return the root node of the BST after the insertion. 
It is guaranteed that the new value does not exist in the 
original BST.

Note that there may exist multiple valid ways for the insertion,
 as long as the tree remains a BST after insertion. You can return 
 any of them.

For example, 

Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
"""


class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def insert(root,val):
            if root.val > val:
                if root.left:
                    insert(root.left,val)
                else:
                    root.left = TreeNode(val)
            elif root.val < val:
                if root.right:
                    insert(root.right,val)
                else:
                    root.right = TreeNode(val)
        insert(root,val)
        return root