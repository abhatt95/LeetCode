# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
Merge two sorted linked lists and return it as 
a new list. The new list should be made by splicing 
together the nodes of the first two lists.
"""

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        head = sol = ListNode(0)
        
        while l1 and l2:
            if l1.val < l2.val:
                current = ListNode(l1.val)
                l1 = l1.next
            else:
                current = ListNode(l2.val)
                l2 = l2.next
            sol.next = current
            sol = sol.next
        while l1:
            current = ListNode(l1.val)
            l1 = l1.next
            sol.next = current
            sol = sol.next
        while l2:
            current = ListNode(l2.val)
            l2 = l2.next
            sol.next = current
            sol = sol.next
        return head.next
