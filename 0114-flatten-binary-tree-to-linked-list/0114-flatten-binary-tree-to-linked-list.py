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
        cases:
            - empty node
            - leaf node
            - no left subtree
            - if left subtree reorder tree

            1
        /.      \
                2        
                 \        
                    3        
                    \
                   4
                        \
                        5
                        \
                        6

    1. Make right ptr of right most node in left subtree: right subtree
    2. Make left subtree cur node's right subtree
    3. set node's left subtree to null
        '''
        def isLeaf(node):
            return not node.left and not node.right
        
        if not root or isLeaf(root):
            return root

        self.flatten(root.left)
        self.flatten(root.right)
        if root.left:
            rightMost = root.left
            while rightMost.right:
                rightMost = rightMost.right
            rightMost.right = root.right
            root.right = root.left
            root.left = None

