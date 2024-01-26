# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        - root can be null => []
        - can be duplicate values
        - nodes with same row and col prioritize left node
        
        IDEA: BFS to get vertical order of Tree
            3 (0)
            /\
         9      20
          \      /\
           10  15  7
            
            
        maintian q (node, colIdx)
        nodeColumns = {column Index: [node values at that column]}
        
        {
            0: [3, 15]
            -1: [9]
            1: [20]
            2: [7]
            
        }
        
        Loop through column indices in map from lowest index to highest (right -> left)
            initialize my ouptut
            
        time: O(n + log(width of tree)) n is nodes in tree
        space: O(n) for q and hashmap
        '''
        # EDGE CASE
        if not root:
            return []
        # BFS
        nodeCols = collections.defaultdict(list) # {node col: [values]}
        q = collections.deque([(root, 0)])
        while q:
            cur, col = q.popleft()
            nodeCols[col].append(cur.val)
            if cur.left:
                q.append((cur.left, col-1))
            if cur.right:
                q.append((cur.right, col+1))
        output = []
        for col in sorted(nodeCols.keys()):
            output.append(nodeCols[col])
        return output
            
        