# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        '''
        Find all nodes with coins store in q

        3 parts:
            1. Convert tree to graph
                - count nodes
                - stores nodes with >= 1 coin in graph
            2. Distribute coins through BFS in graph
                - We know there are n total coins so they must be distributed somewhere
                - Loop through q of nodes with coins
                - if c is coins that node initially had, distribute coins to c - 1 nodes and incremenet minMoves by lenght of path to all nodes distributed to
                return minMoves

                Time Complexity: O(V + E) => O(V + (V-1)*2)
                Space Complexity: O(V) to store array

        '''

        graph = collections.defaultdict(list)
        q = collections.deque([root])
        nodes_to_coin = {}
        while q:
            cur = q.popleft()
            if cur.left:
                graph[cur].append(cur.left)
                graph[cur.left].append(cur)
                q.append(cur.left)
            if cur.right:
                graph[cur].append(cur.right)
                graph[cur.right].append(cur)
                q.append(cur.right)
        movesNeeded = 0
        for node in sorted(graph.keys(), key = lambda x: x.val, reverse = True):
            # No coins to distribute
            if node.val in [1,0]:
                break
            # We have a node with >= 2 coins
            # BFS to find closes nodes
            q = collections.deque([node])
            visited = {node}
            pathLength = 0
            while q and node.val > 1:
                for _ in range(len(q)):
                    cur = q.popleft()
                    # Check if we can give this node a coin
                    if cur.val == 0:
                        cur.val += 1
                        node.val -= 1
                        movesNeeded += pathLength

                    if node.val == 1:
                        break
                    # Careful not to go backwards but will not cycle
                    for nei in graph[cur]:
                        if nei not in visited:
                            q.append(nei)
                            visited.add(nei)


                pathLength += 1
        return movesNeeded

            
        

        