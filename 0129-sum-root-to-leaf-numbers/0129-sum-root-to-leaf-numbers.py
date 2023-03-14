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
            if not node.right and not node.left:
                ans += curSum
                return
            if node.left:
                dfs(node.left, curSum)
            if node.right:
                dfs(node.right, curSum)
            
        
        dfs(root, 0)
        return ans
        