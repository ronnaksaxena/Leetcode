# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        '''
        dfs(node1, node2)
            if both null:
                return True
            if one null
                return false
            if n1.val != n2.val:
                return false
            if dfs(node1.left, node2.left) or dfs(node1.left, node2.right) or dfs(node1.right, node2.left) or dfs(node1.right, node2.right):
                return True


        1                           1
        / \                       /.   \
        2 3                        3       2
    /.  \. /                        \       /   \
    4.  5. 6                        6      4    5
       /. \                                     /   \
       7. 8                                     8   7


        '''

        def dfs(n1, n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2:
                return False
            if n1.val != n2.val:
                return False
            return (dfs(n1.left, n2.left) and dfs(n1.right, n2.right)) or (dfs(n1.right, n2.left) and dfs(n1.left, n2.right))

        return dfs(root1, root2)
        