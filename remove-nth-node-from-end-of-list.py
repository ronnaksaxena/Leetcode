# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return head
        dummy = a = b = ListNode(0, head)
        for _ in range(n):
            a = a.next
        
        while a.next:
            b = b.next
            a = a.next
        
        b.next = b.next.next
        return dummy.next
