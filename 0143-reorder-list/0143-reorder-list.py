# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        
        """
        if not head or not head.next:
            return
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        # Rev slow
        prev, cur = None, slow
        while cur:
            cur.next, cur, prev = prev, cur.next, cur
        # prev is mid of list
        first, second = head, prev
        # second.next becuase once you are at last element in list all elems are reordered
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
        return
            
        