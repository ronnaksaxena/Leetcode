# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            return dfs(node.left) + [node.val] + dfs(node.right) if node else []
        vals = dfs(root)
        ans = float('inf')
        for i in range(len(vals)-1):
            ans = min(ans, abs(vals[i+1]-vals[i]))
        return ans
        