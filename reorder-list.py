# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def revList(self, head):
        if not head or not head.next:
            return head
        p = self.revList(head.next)
        head.next.next = head
        head.next = None
        return p
    
        
        
        
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        revHalf = self.revList(slow)
        
        first, second = head, revHalf
        while second.next:
            temp = first.next
            first.next = second
            first = temp
            
            temp = second.next
            second.next  = first
            second = temp
            
        return head
            
        
        
        
