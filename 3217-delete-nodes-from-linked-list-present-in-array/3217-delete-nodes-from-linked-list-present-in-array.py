# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy = prev = ListNode(0)
        dummy.next = head
        cur = head

        numsSet = set(nums)
        while cur:
            while cur and cur.val in numsSet:
                cur = cur.next
            prev.next = cur
            prev, cur = cur, cur.next
        
        return dummy.next

        