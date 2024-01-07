# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        '''
        input: node, int, int
        output: int
        - Root can be null
        - inclusive low, high
        
        DFS
        - check if nodes value is in range
            - increment total sum by node value
        
        Time: O(n)
        Space: O(h)
        
        Optimizations:
        - traverse inorder dfs
        - once we enounter value > hi: return
        
        Algo:
        totalSum = 0
        
        dfs (node)
            - make totalSum global
            - if node is null: return
            - rec call on left
            - if node value in range:
                increment our totalSum value
            - if node vale > hi: return => prune tree
            rec call on right subtree
        call dfs
        return totalSum
        
        '''
        totalSum = 0
        def dfs(node):
            nonlocal totalSum
            if not node:
                return
            dfs(node.left)
            if low <= node.val <= high:
                totalSum += node.val
            elif node.val > high:
                return
            dfs(node.right)
        dfs(root)
        return totalSum
            
            
            
            
            
            
            
            
        