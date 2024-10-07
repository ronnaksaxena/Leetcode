# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        count = 0
        for l in lists:
            if not l:
                continue
            heapq.heappush(heap, (l.val, count, l))
            count += 1

        dummy = ListNode(0)
        cur = dummy

        while heap:
            _, _, nextNode = heapq.heappop(heap)
            cur.next = nextNode
            cur = cur.next
            count += 1
            if nextNode.next:
                heapq.heappush(heap, (nextNode.next.val, count, nextNode.next))
        
        return dummy.next
            
        