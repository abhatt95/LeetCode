# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Given two non-empty binary trees s and t, 
check whether tree t has exactly the same structure
and node values with a subtree of s. A subtree of s
is a tree consists of a node in s and all of this
node's descendants. The tree s could also be considered
as a subtree of itself.
"""

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        
        # check if two trees are same. 
        def check(s,t):
            if not s and not t:
                return True
            if s and t:
                if s.val == t.val:
                    return check(s.left,t.left) and check(s.right,t.right)
            return False
        
        # BFS traversal on q, if values of node are same than start checking if subtree are same.
        queue = [s]
        while queue:
            current = queue.pop(0)
            if current:
                if current.val == t.val:
                    if check(current,t):
                        return True
            
                queue.append(current.left)
                queue.append(current.right)
        return False
            