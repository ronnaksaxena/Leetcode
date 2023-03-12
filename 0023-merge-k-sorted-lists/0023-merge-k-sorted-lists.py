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
                heapq.heappush(heap, (l.val, cnt, l))
                cnt += 1
                l = l.next
        dummy = ListNode(0)
        cur = dummy
        while heap:
            _, _, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next

        return dummy.next

