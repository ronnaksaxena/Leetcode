"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
        Input: Node
        Output: Node

        -Yes connected graph
        -No self loops
        -Can be null
        - unique values

        Idea: Traverse adn init deep copies of each node
        - Store in memeory nodes already created
        - Return root nodes

        Algo: DFS search
        map {nodeVal: node}
        help fn (node, map of created nodes)
            1. if node is null: return null -> edge case
            2. if node.val in map: return map[node val]
            3. newNode = node.val
            4. map[node.val] = newNode
            5. newNode.neighbors = [helper(neighbor, map) for neighbor in node.neighbors]
            return newNode

        return helper(root, {})

        Time: O(V+E) V is nodes in map, E is edges iterte through
        Sapce: O(V) for hashmap
        '''

        def helper(node, createdNodes):
            if not node:
                return None
            if node.val in createdNodes:
                return createdNodes[node.val]
            newNode = Node(node.val)
            createdNodes[node.val] = newNode
            newNode.neighbors = [helper(nei, createdNodes) for nei in node.neighbors]
            return newNode
        return helper(node,{})