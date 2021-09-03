# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        def isSame(s,t):
            if not s and not t:
                return True
            elif not s or not t:
                return False
            return s.val == t.val and isSame(s.left,t.left) and isSame(s.right,t.right)
        
        def traverse(s,t):
            if not s and not t:
                return True
            elif not s and t:
                return False
            elif s and not t:
                return False
            else:
                if s.val != t.val:
                    return traverse(s.left,t) or traverse(s.right,t)
                else:
                    if traverse(s.left,t) or traverse(s.right,t):
