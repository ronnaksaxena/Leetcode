# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = None
        
        def dfs(node):
            nonlocal lca
            if not node:
                return False
            left = dfs(node.left)
            right = dfs(node.right)
            
            if (node in [p,q]) + left + right >= 2 and not lca:
                lca = node
            
            return node in [p,q] or left or right
        
        dfs(root)
        return lca