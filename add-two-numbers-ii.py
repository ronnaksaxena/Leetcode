# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDigits(self, node) -> List[str]:
        if not node:
            return []
        return [str(node.val)] + (self.getDigits(node.next))
        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1Digits = self.getDigits(l1)
        l2Digits = self.getDigits(l2)
        l1Num = int("".join(l1Digits))
        l2Num = int("".join(l2Digits))
        sumNum = l1Num + l2Num
        head = point = ListNode(0)
        for i in [int(d) for d in str(sumNum)]:
            point.next = ListNode(i)
            point = point.next
        return head.next
        
