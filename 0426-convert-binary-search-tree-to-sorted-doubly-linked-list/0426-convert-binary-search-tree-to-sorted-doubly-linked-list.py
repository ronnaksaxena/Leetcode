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
        # EDGE CASE
        if not root:
            return None
        head, tail = None, None
        def dfs(node):
            nonlocal head, tail
            if not node:
                return
            
            dfs(node.left)
            if not head:
                head = node
                tail = node
            else:
                tail.right, node.left = node, tail
                tail = node

            dfs(node.right)

        dfs(root)
        # Complete cycle
        tail.right, head.left = head, tail
        return head
        