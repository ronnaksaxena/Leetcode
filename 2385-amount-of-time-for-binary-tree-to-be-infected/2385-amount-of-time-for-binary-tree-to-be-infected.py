# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        '''
        - start in root
        - unique values in root
        - single node case takes 1 secons
        
        Idea: Create graph and BFS
        - Traverse tree and initialize graph in process
        - Have ptr to patient0 if val == start
        - BFS starting at patient0
            - keep track of depth to expand search
        - return depth
        
        Time: O(N + E) Edges in tree are Nodes - 1 => N + N-1 => N
        Space: O(N) for dicitonary adjlist list and visited set
        
        
        '''
        # Create Graph
        graph = collections.defaultdict(list)
        patinet0 = None
        q = collections.deque([root])
        while q:
            cur = q.popleft()
            # Check for start node
            if cur.val == start:
                patient0 = cur
            if cur.left:
                # Connect nodes
                graph[cur].append(cur.left)
                graph[cur.left].append(cur)
                q.append(cur.left)
            if cur.right:
                graph[cur].append(cur.right)
                graph[cur.right].append(cur)
                q.append(cur.right)
        # Traverse graph and find infection time
        minutes = -1
        q = collections.deque([patient0])
        visited = {patient0}
        while q:
            # Loop through layer
            for _ in range(len(q)):
                cur = q.popleft()
                for nei in graph[cur]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
            minutes += 1
        
        return minutes
            
                
        