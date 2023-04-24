# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = set()
        dummy = cur = ListNode(0)
        while head:
            if head.val not in vals:
                cur.next = head
                cur = cur.next
                vals.add(head.val)
            head = head.next
        
        cur.next = None
            
        return dummy.next
                
        
        