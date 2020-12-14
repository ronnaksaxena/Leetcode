"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
​
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        q = []
        q.append(root)
        numTraversed = 0
        level = 1
        while q:
            lastNode = 2**level-1
            for i in range(len(q)):
                cur = q.pop(0)
                numTraversed += 1
                if numTraversed==lastNode:
                    cur.next = None
                else:
                    cur.next = q[0]
                if cur.left:
                    q.append(cur.left)
