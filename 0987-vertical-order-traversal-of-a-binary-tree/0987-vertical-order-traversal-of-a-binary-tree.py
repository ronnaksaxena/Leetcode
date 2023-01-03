# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        '''
         3
        / \
       9.  20
           / \
          15. 7
        (node val, row, col)
        q = [(9, 1, -1)]

        cols = {col: row : [node values]} index is row order
        0 : {0 : [3]}
        -1 : {1 : [9]}
        # Time: O(n) where n is nodes in tree
        # Space: O(n) where n is nodes in tree for queue and hashmap
        '''

        cols = {}
        q = collections.deque([(root, 0, 0)])
        output = []
        # Find columns of nodes
        while q:
            node, row, col = q.popleft()
            if col in cols:
                if row in cols[col]:
                    cols[col][row] += [node.val]
                else:
                    cols[col][row] = [node.val]
            else:
                cols[col] = {row : [node.val]}
            if node.left:
                q.append((node.left, row + 1, col -1))
            if node.right:
                q.append((node.right, row + 1, col + 1))
        # Construct output in order of cols
        for col in sorted(cols.keys()):
            nodesInColumn = []
            for row in cols[col]:
                # Sort nodes that appear in same row and col
                cols[col][row].sort()
                nodesInColumn += cols[col][row]
            output.append(nodesInColumn)

        return output


