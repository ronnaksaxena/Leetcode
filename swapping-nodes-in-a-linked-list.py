# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        '''
       d [1,2,3,4,5], k = 2
                   f
                s
              p1
            i
          p2
        
        
        '''
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        f, s = head, head
        p1,p2 = dummy, dummy
        
        for _ in range(k):
            f = f.next
        
        while f:
            f = f.next
            s, p2 = s.next, p2.next
            
        i = head
        for _ in range(k-1):
            i, p1 = i.next, p1.next
        #swap nodes
        s.val, i.val = i.val, s.val
        
        
        return head
        
        
        
        
