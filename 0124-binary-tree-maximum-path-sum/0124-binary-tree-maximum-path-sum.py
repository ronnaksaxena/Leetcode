# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        -10
       /. \     
    -100.  -10

        '''
        # EDGE CASE
        if not root:
            return 0

        maxSum = float(-inf)
        def dfs(node):
            nonlocal maxSum
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            maxSum = max(maxSum, node.val + left, node.val + right, node.val + left + right, node.val)
            return node.val + max(left, right)

        dfs(root)
        return maxSum
            
        