"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        '''
        Idea: two pointer traversal to find insertion
        
        EDGE CASE: empty list -> create new node and return
        EDGE CASE: singleton list -> have head next point to new element
        
        loop while cur.next != head
            - check for prev.val <= insertVal <= cur.val:
                init new node and connect ptrs
                return head
            - check if at edge of list
                cur.val > cur.next.val and insertVal < cur.next.val
            
        
        '''
        # empty list
        if not head:
            node = Node(insertVal)
            node.next = node
            return node
        cur = head
        while cur.next != head:
            if cur.val <= insertVal <= cur.next.val:
                node = Node(insertVal, cur.next)
                cur.next = node
                return head
            # Insert node at edge of list
            if (cur.val > cur.next.val) and (insertVal < cur.next.val or insertVal > cur.val):
                node = Node(insertVal, cur.next)
                cur.next = node
                return head
            cur = cur.next
        # All elements in list are same
        # Insert anywhere
        node = Node(insertVal,cur.next)
        cur.next = node
        return head
                
        