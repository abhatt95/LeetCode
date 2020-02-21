"""
    You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    """
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
            :type l1: ListNode
            :type l2: ListNode
            :rtype: ListNode
            """
        
        result = ListNode(0)
        resultTail = result
        carry = 0
        
        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry,s = divmod(val1+val2+carry,10)
            
            resultTail.next = ListNode(s)
            resultTail = resultTail.next
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
    
        return result.next
