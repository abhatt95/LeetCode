"""
    Given two binary search trees, return True if and only if there is a node in the first tree and a node in the second tree whose values sum up to a given integer target.
    """
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def twoSumBSTs(self, root1, root2, target):
        """
            :type root1: TreeNode
            :type root2: TreeNode
            :type target: int
            :rtype: bool
            """
        
        nodes = []
        def inorder(root):
            if root:
                inorder(root.left)
                nodes.append(root.val)
                inorder(root.right)
    
        inorder(root1)
        firsttree = set(nodes)
        
        nodes = []
        inorder(root2)
        
        for node in nodes:
            if target-node in firsttree:
                return True

                    return False
