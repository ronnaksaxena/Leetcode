# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node, curSum):
            nonlocal ans
            if not node:
                return
            curSum = (curSum * 10) + node.val
            # Don't want to process paths twice so stop once at a leaf
            if not node.right and not node.left:
                ans += curSum
                return
            dfs(node.left, curSum)
            dfs(node.right, curSum)
        dfs(root, 0)
        return ans
        '''
        Time: O(n) for n nodes in tree
        Space: O(h) where h is height of tree for recurisve stack
        '''