# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(cur):
            if not cur:
                return None
            left = dfs(cur.left)
            right = dfs(cur.right)
            cur.left, cur.right = right, left
            return cur

        dfs(root)
        return root
        