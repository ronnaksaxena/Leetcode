# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        input: root node of tree
        output: root node of inverted tree

        EDGE CASES:
        - if null return null
        - valid input
        - not garunteed to be unique
        - Doesn't have to be in place


        intuition: post order traversal

                2                           2
            /       \.          =>        /.    \
            1       3                   3       1

        root.right = left
        root.left = right

                4
            /.     \
            7       3
        /       \. /.  \
        9       6. 2.   1


        PSUEDODE:

        if null tree:
            return null
        
        leftSubTree = dfs(root.left)
        rightSubtree = dfs(root.right)

        root.right = leftSubTree
        root.left = rightSubtree
        return root

        Time O(n) -> traverse all nodes in tree
        Sapce: O(h) -. h is heihgt of the tree for recursive stack
        '''

        if not root:
            return None
        leftSubTree = self.invertTree(root.left)
        rightSubTree = self.invertTree(root.right)

        root.right = leftSubTree
        root.left = rightSubTree
        return root

        