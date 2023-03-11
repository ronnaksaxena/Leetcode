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
        Time: O(n) to process every node in list
        Space: O(logn) height will be log2 of size of list
        '''
        # Start is inclusive, end is exclusive
        def helper(start, end):
            # No nodes in this subtree
            if start == end:
                return None
            # Find middle node to make root
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
        