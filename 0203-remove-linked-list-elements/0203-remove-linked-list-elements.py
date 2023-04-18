# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        '''
        val = 6
        [1,2,6,3,4,5,6]
           p
               c
        '''
        cur, prev = head, None
        while cur:
            while cur.val == val:
                cur = cur.next
                if prev:
                    prev.next = cur
                else:
                    head = cur
                if not cur:
                    return head
            prev, cur = cur, cur.next
        
        return head
        