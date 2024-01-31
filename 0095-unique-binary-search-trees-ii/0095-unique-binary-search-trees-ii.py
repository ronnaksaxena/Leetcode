# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        @cache
        def backtrack(l, r):
            if l > r:
                return [None]
            res = []
            for rootVal in range(l, r+1):
                for leftSubtree in backtrack(l, rootVal-1):
                    for rightSubtree in backtrack(rootVal+1, r):
                        root = TreeNode(rootVal, leftSubtree, rightSubtree)
                        res.append(root)
            return res
        
        return backtrack(1, n)
                        
                
        