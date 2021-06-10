"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
​
class Solution:
    #instance var for visited
    def __init__(self):
        self.visited = collections.defaultdict()
        
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        if node in self.visited.keys():
            return self.visited[node]
        
        newNode = Node(node.val,[])
        self.visited[node] = newNode
        
        if node.neighbors:
            newNode.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        
        return newNode
