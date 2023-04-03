# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        -10
      /.   \
     9.    20
          /. \
         15.  7
         
    max path is either:
    1. just current node
    2. left
    3. right
    4. node + left + right
    
    bottom up solution 
    Time: O(n)
    Space: O(1)
        
        '''
        maxPath = float('-inf')
        def dfs(node):
            nonlocal maxPath
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            maxPath = max(maxPath, node.val, node.val + left, node.val + right, node.val + left + right)
            return max(node.val + left, node.val + right, node.val)
            
        dfs(root)
        return maxPath
            
            
            
            
            
            
            