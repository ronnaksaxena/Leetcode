# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.helper(l1,l2,0)
    
    def helper(self, l1, l2, carry):
        if not l1 and not l2 and carry==0:
            return None
        if not l1 and carry==0:
            return l2
        if not l2 and carry==0:
            return l1
        summation = 0
        summation += l1.val if l1 else 0
        summation += l2.val if l2 else 0
        summation += carry
        digit = summation%10
        carry = summation//10
        return ListNode(digit, self.helper(l1.next if l1 else None,l2.next if l2 else None, carry))
