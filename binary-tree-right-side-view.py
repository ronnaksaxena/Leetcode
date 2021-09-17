# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        output = []
        q = collections.deque()
        q.append(root)
        
        while q:
            size = len(q)
            for i in range(len(q)):
                cur = q.popleft()
                
                if i == size-1:
                    output.append(cur.val)
                    
                if cur.left:
                    q.append(cur.left)
                    
                if cur.right:
                    q.append(cur.right)
                    
        return output
