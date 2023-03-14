# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        def dfs(node, curSum):
            nonlocal ans
            if not node:
                return
            curSum = (curSum * 10) + node.val
            # Don't want to process paths twice so stop once at a leaf
            if not node.right and not node.left:
                ans += curSum
                return
            # Want to ignore children that are null
            if node.left:
                dfs(node.left, curSum)
            if node.right:
                dfs(node.right, curSum)
            
        
        dfs(root, 0)
        return ans
        