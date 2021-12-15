# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        '''
        6 5 3 1 8 7 2 4
          c
-inf    5 6
​
        d
p
        
        '''
        
        if not head:
            return head
        
        dummy = ListNode(float('-inf'))
        cur = head
        
        while cur:
            
            prev = dummy
            
            while prev.next and prev.next.val < cur.val:
                prev = prev.next
                
            next = cur.next
            
            cur.next = prev.next
            prev.next = cur
            
            cur = next
            
            
        return dummy.next
            
            
            
                
                
                
                
                
