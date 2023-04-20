# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        res = 0
        @cache
        def dfs(node, goLeft, streak):
            nonlocal res
            if node:
                res = max(res, streak)
                if goLeft:
                    dfs(node.left, False, streak+1)
                    dfs(node.right, True, 1)
                else:
                    dfs(node.right, True, streak+1)
                    dfs(node.left, False, 1)
            
            
        
        dfs(root, True, 0)
        dfs(root, False, 0)
        return res
        