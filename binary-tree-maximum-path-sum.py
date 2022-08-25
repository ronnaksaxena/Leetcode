# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Edge Case if empty root
        if not root:
            return 0
        
        maxSum = float('-inf')
        # Bottom up traversal to find max path
        def dfs(node, pathSum):
            nonlocal maxSum
            if not node:
                return pathSum
            left = dfs(node.left, pathSum)
            right = dfs(node.right, pathSum)
            # Need 0 to handle case of negative path
            leftMax = max(left, 0)
            rightMax = max(right, 0)
            # Check new max path is found
            maxSum = max(maxSum, node.val + leftMax + rightMax)
            # Return greater subtree path for other calls
            return node.val + max(leftMax, rightMax)
        
        dfs(root, 0)
        return maxSum
        
        
