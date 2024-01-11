# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        maxDiff = 0
        def dfs(node, lo = inf, hi = -inf):
            nonlocal maxDiff
            if not node:
                return
            curLo = min(lo, node.val)
            curHi = max(hi, node.val)
            maxDiff = max(maxDiff, abs(curHi - curLo))
            dfs(node.left, curLo, curHi)
            dfs(node.right, curLo, curHi)
            
            return
        dfs(root)
        return maxDiff
        