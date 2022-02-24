# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        heap = []
        
        dummy = cur = ListNode(0)
        
        count = 0
        while head:
            heapq.heappush((heap), (head.val, count, head))
            head = head.next
            count += 1
            
        while heap:
            _,_,node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
        cur.next = None
            
        return dummy.next
        
