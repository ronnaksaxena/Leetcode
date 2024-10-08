# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''

      <-  1 <- 2 <- 3 
                       c
                    p

        '''

        prev, cur = None, head
        while cur:
            cur.next, cur, prev = prev, cur.next, cur

        return prev
        