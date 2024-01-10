# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        Output: Integer
        
        - Not null root
        - Single node has diameter of 0
        - Diameter does not have to pass throught root
        
        
        Idea: Bottom Up Post Order DFS
        Diameter of current node is 1 + height of subtree
        maxDiameter = 0
        helper fn dfs(node)
            - if null: return 0
            left = -1
            right = -1
            if left subtree: 
                rec call on left
            if right subtree: 
                rec call on right
            maxDiameter = max(maxDiameter, 1 + left + 1 + right)
            return height => 1 + max(left, right)
        call dfs
        return maxDiameter
        
        1 l = 0, r = -1, d = 1, h
      /
     2 l -1, r -1, d= 0, h = 0
     
        
        Time: O(n) where n is number of nodes
        Space: O(h) rec stack h is heigh of tree
        
        '''
        maxDiameter = 0
        def dfs(node):
            nonlocal maxDiameter
            if not node:
                return 0
            left = -1
            right = -1
            if node.left:
                left = dfs(node.left)
            if node.right:
                right = dfs(node.right)
            maxDiameter = max(maxDiameter, 1 + left + 1 + right)
            # Return height
            return 1 + max(left, right)

        dfs(root)
        return maxDiameter
        