# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        leftBound = dummy

        # move leftBound to node before first node to reverse
        for i in range(left-1):
            leftBound = leftBound.next

        # garutneed not null due to constraints
        cur = leftBound.next
        newTail = cur
        # reverse nodes in range left -> right
        newHead = None
        for _ in range(right-left+1):
            # print(newHead.val if newHead else 'None', cur.val)
            cur.next, cur, newHead = newHead, cur.next, cur
        # connect bounds
        leftBound.next = newHead
        newTail.next = cur

        return dummy.next


        
        