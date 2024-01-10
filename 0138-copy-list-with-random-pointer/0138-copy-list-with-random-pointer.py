"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
        [[7,null],[13,0],[11,4],[10,2],[1,0]]
        
        - can be pointed to by multiple randomm pointers
        - no cycle in list
        - head can be null
        - random can point to itself
        - don't want duplicate nodes
        
        Idea: Iterate throught list and hash copies of nodes
        {originalNode: copyNode}
        
        helper fn copyList(node):
            - Base case null node: return Null
            - check if created copy from hash map
                if created return copy
            - create new copy
            - add it cache / hash map
            - next = copyList(node.next),  random = copyList(node.random)
            - return node
        Time: O(n)
        Space: O(n) for recurisive stack & hash map
        
        '''
        originalToCopy = {} # Original Node : Copy Node
        
        def copyList(node):
            if not node:
                return None
            # Check if node was copied already
            if node in originalToCopy:
                return originalToCopy[node]
            # Copy node
            copyNode = Node(node.val)
            originalToCopy[node] = copyNode
            copyNode.next = copyList(node.next)
            copyNode.random = copyList(node.random)
            return copyNode
        
        return copyList(head)
        
        
        
        
        
        