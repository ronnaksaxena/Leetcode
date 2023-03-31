# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        1 -> 2 -> 3 -> 4 -> 5 ->
                  a
                            b
        move b up n times
        move both up until b.next (at last node)
        remove a's next node
        Time O(n)
        Space O(n)
        '''
        a, b = head, head
        for _ in range(n):
            b = b.next
        # EDGE CASE: removing first node
        if not b:
            return a.next
        while b.next:
            a, b = a.next, b.next
        a.next = a.next.next
        return head