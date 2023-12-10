# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # Egdge case no tree
        if not root:
            return True
        q = collections.deque([root])
        foundNullNode = False
        while q:
            cur = q.popleft()
            if cur is None:
                foundNullNode = True
            else:
                if foundNullNode:
                    return False
                q.append(cur.left)
                q.append(cur.right)
        return True
            
        