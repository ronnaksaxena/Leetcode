# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        slow, fast = head, head
        intersect = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                intersect = slow
                break
        # No intersection
        if intersect == None:
            return None
        # Need to find start of cycle
        slow = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast
        
        