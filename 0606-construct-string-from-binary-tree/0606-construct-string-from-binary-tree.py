# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, t: Optional[TreeNode]) -> str:
        '''
        1
        /\
    2       3
    /\
4

s += node.val
if left:
    s += ( + dfs(left) + )
if right:
    s += ( + dfs(right) + )
return s
        
        '''
        if not t:
            return ""
        elif not t.left and not t.right:
            return str(t.val)
        elif not t.right:
            s = self.tree2str(t.left)
            return str(t.val)+"("+s+")"
        elif not t.left:
            s = self.tree2str(t.right)
            return str(t.val)+"()"+"("+s+")"
        l = self.tree2str(t.left)
        r = self.tree2str(t.right)
        return str(t.val)+"("+l+")"+"("+r+")"
        