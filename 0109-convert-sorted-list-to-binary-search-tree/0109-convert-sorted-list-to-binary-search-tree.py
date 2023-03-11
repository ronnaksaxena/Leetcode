# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        '''
        -10 -> -3 -> 0 -> 5 -> 9
                     e
        s
                e
          
                    0
                   / \
                  -3
                 / \
               -10 None
        
        BASE CASES:
        if start == end: return None
        if not start and not end: return None
        otherwise make node from middle and recruse
        fast, slow = start, start
        while fast != end.next and fast.next != end.next:
            fast = fast.next.next
            slow = slow.next
        mid = TreeNode(slow.val)
        mid.left = rec(start)
        mid.right = rec(slow.next)
        return mid
        '''
        def helper(start, end):
            if start == end:
                return None
            if not start and not end:
                return None
            slow, fast = start, start
            while fast != end and fast.next != end:
                slow = slow.next
                fast = fast.next.next
            # slow is at mid
            root = TreeNode(slow.val)
            root.left = helper(start, slow)
            root.right = helper(slow.next, end)
            return root
        
        
        return helper(head, None)
        