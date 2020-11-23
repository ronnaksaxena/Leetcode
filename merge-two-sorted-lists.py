# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        elif l1 and not l2:
            return l1
        elif l2 and not l1:
            return l2
        elif l1.val < l2.val:
            return ListNode(l1.val, self.mergeTwoLists(l1.next,l2))
        else:
            return ListNode(l2.val, self.mergeTwoLists(l1,l2.next))
