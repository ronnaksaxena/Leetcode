# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        prev = None
        cur = head
        while cur:
            nextTemp = cur.next
            cur.next = prev
            prev = cur
            cur = nextTemp
        return prev
