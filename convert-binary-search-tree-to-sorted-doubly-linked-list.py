"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
​
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        head, tail = None, None
        
        stack = collections.deque()
        cur = root
        
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
                
            cur = stack.pop()
            
            if not head:
                head = cur
            else:
                tail.right = cur
                cur.left = tail
                
            tail = cur
            cur = cur.right
            
        
        head.left, tail.right = tail, head
        
        return head
        
        
        
        
                
                
                
                
                
