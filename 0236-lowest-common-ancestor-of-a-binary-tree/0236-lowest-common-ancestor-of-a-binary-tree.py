# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        - p and q in tree
        - p != q
        - valid binary tree
        
        Idea: post order traversal
        
        3
     /      \
   5        1
    /\     / \ 
  6.  2   0.  8
     /\
     7 4
     
     LCA:
        - cur node is p: q is a child
        - cur node is q & p is a child
        - p and q are in left and right sub trees respectively
    
    LCA = None # global
    dfs helper -> Bool (have we encountered p or q yet)
        - if empty node:
            false
        - left = dfs(node.left)
        - right = dfs(node.right)
        if (node in [p,q]) + left + right >= 2 and LCA == None:
            LCA = node
        return node == p or node == q or left or right
    
    call dfs
    return LCA
    
    Time: O(n) where n is nodes in tree
    Space: O(h) where h is height of tree
        
        '''
        
        LCA = None
        def dfs(node):
            nonlocal LCA
            if not node:
                return False
            left = dfs(node.left)
            right = dfs(node.right)
            
            # Check if possible LCA
            if (node in [p,q]) + left + right >= 2 and (not LCA):
                LCA = node
            # Tell parent we encountered p or q
            return (node in [p,q]) or left or right
        dfs(root)
        return LCA
                
        