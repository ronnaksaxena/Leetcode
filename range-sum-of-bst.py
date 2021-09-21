# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        stack = []
        sum = 0
        cur = root
        
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
                
            cur = stack.pop()
            
            if low <= cur.val <= high:
                sum += cur.val
            
            cur = cur.right
            
