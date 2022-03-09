# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev = dummy = ListNode(0, head)
        prev.next = head
        cur = head
        
        while cur:
            if cur.next and cur.next.val == cur.val:
                curVal = cur.val
                while cur and cur.val == curVal:
                    cur = cur.next
                prev.next = cur
            else:
                prev, cur = cur, cur.next
            
        return dummy.next
        
        
