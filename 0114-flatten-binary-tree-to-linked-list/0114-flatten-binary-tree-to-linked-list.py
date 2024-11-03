# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        '''
        1
        / \
        2. 5
    /.  \.   \
    3.  4.   6

        Steps: Post order traversal
        Find right most node of left subtree
        rightNode.right = curNode.right
        curNode.right = curNode.left
        curNode.left = None

        return head to parent
        '''

        def dfs(node):
            if not node:
                return None
            
            left = dfs(node.left)
            right = dfs(node.right)

            # Have tail of left subtree point to right subtree
            if left:
                rightMost = left
                while rightMost.right:
                    rightMost = rightMost.right
                rightMost.right = right
                node.right = left
                node.left = None
            return node

        dfs(root)
        return None

        
        