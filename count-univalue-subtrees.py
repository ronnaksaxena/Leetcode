# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        
        count = 0
        
        def dfs(root, val):
            nonlocal count
            if not root:
                return True
            
            if not all([dfs(root.left, root.val), dfs(root.right, root.val)]):
                return False
            
            count += 1
            
            return root.val == val
        
        dfs(root, 0)
        return count
        
