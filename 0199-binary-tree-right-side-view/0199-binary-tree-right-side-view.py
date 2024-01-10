# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        input: TreeNode
        output: [ints]
        
        if root null: return empty list
        
        Idea: BFS
        - traverse tree by levels
        - when at last node in level, add value to output list
        
        Time: O(N) n is number of nodes
        Sapce: O(N) for queue
        '''
        # Edge case empty tree
        if not root:
            return []
        
        q = collections.deque([root])
        output = []
        
        # BFS
        while q:
            nodesInLevel = len(q)
            for i in range(nodesInLevel):
                node = q.popleft()
                if i == nodesInLevel - 1:
                    output.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return output
        