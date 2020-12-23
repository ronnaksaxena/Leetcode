# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        candidate = None
        cur = root
        
        while cur:
            if cur.val > p.val:
                candidate = cur
                cur = cur.left
            else:
                cur = cur.right
        return candidate
