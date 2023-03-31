# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []
        cnt = 0
        
        for l in lists:
            while l:
                heapq.heappush(heap, (l.val, cnt))
                l = l.next
        dummy = cur = ListNode(0)
        while heap:
            val, _ = heapq.heappop(heap)
            cur.next = ListNode(val)
            cur = cur.next
            
        return dummy.next
            
            