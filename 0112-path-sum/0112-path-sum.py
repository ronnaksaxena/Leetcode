# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, pathSum):
            if not node.left and not node.right:
                return (node.val + pathSum) == targetSum
            left = dfs(node.left, node.val+ pathSum) if node.left else False
            right = dfs(node.right, node.val + pathSum) if node.right else False
            
            return left or right
        
        return dfs(root, 0) if root else False
        