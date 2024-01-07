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
        
        def dfs(root):
            nonlocal head
            nonlocal tail
            stack = []
            cur = root
            while stack or cur:
                while cur:
                    stack.append(cur)
                    cur = cur.left
                cur = stack.pop()
                if not head:
                    head = cur
                if tail:
                    tail.right = cur
                cur.left = tail
                tail = cur
                cur = cur.right
            
        dfs(root)
        # Connect tail and head
        head.left, tail.right = tail, head
        return head
            
        