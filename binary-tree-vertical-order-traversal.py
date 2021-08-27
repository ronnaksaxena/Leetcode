# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        columns = collections.defaultdict(list)
        self.generateCols(root, columns)
        output = []
        for col in sorted(columns.keys()):
            output.append(columns[col])
            
        return output
        
    def generateCols(self, root, columns):
        q = collections.deque([(root,0)])
        
        while q:
            cur, val = q.popleft()
            columns[val].append(cur.val)
            
            if cur.left:
                q.append((cur.left, val-1))
            if cur.right:
                q.append((cur.right, val+1))
        
    
            
        
