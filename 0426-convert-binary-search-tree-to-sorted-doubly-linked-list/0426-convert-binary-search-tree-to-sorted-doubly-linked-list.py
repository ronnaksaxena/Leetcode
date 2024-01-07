"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        '''
            4
        /.      \
        2       5
    /       \
1           3
        
        h 1
        t 1
        
        '''
        if not root:
            return root
        head, tail = None, None
        
        def dfs(node):
            nonlocal head
            nonlocal tail
            if not node:
                return
            dfs(node.left)
            # process node
            if not head:
                head = node
            if tail:
                tail.right = node
            node.left = tail
            tail = node
            dfs(node.right)
            
        dfs(root)
        # Connect tail and head
        head.left, tail.right = tail, head
        return head
            
        