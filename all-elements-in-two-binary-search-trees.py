# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        res = []
        stack = []
        cur = root1
        
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
                
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
            
        stack = []
        cur = root2
        
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
                
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
            
        res.sort()
        return res
            
            
        
