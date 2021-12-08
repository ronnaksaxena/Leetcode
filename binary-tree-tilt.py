# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.totalTilt = 0
        
        def dfs(root, tilt):
            if not root:
                return 0
            
            left = dfs(root.left, tilt)
            right = dfs(root.right, tilt)
            
            curTilt = abs(left-right)
            self.totalTilt += curTilt
            return root.val + left + right
        
        dfs(root, 0)
        
        return self.totalTilt
