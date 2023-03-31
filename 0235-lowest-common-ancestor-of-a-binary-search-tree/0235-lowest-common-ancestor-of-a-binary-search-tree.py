# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def findLowest(node, A, B):
            if node == A or node == B:
                return node
            if A.val < node.val < B.val:
                return node
            elif A.val < node.val and B.val < node.val:
                return findLowest(node.left, A, B)
            else:
                return findLowest(node.right, A, B)
        
        A, B = (p, q) if p.val < q.val else (q, p)
        
        return findLowest(root, A, B)
        
        