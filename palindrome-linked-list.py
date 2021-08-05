# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def revList(self, head):
        if not head or not head.next:
            return head
        
        pre, cur = None, head
        
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
            
        
        return pre
        
        
        
        
        
    def isPalindrome(self, head: ListNode) -> bool:
        
        if not head or not head.next:
            return True
        
        slow = fast = head
        
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        
        slow = self.revList(slow)
        
        
        
        ptr = head
        
        while slow:
            
            if ptr.val != slow.val:
                return False
            
            ptr, slow = ptr.next, slow.next
            
        
        return True
        
        
