# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        aPtr = headA
        bPtr = headB
        while not aPtr == bPtr:
            aPtr = aPtr.next if aPtr else headB
            bPtr = bPtr.next if bPtr else headA
        return aPtr
