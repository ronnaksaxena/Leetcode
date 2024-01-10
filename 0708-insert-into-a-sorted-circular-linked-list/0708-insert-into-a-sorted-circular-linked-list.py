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
        input: head of single linked list
        output: head of list after insertion
        
        - if null make a single node that points to itself
        - Can be duplicate values and can be 0
        
        Case 1: Null list
        - return insert val node
        
        Case 2: Insert into middle of list
        -return head
        
        Case 3: Insert at edge of list (between smallest and largest)
        
        Case 4: All nodes in list are same value
         
         Time: O(n) where n is nodes in list
         Space: O(1) no extra memory
         
        '''
        # Case 1: empty list
        if not head:
            insertValNode = Node(insertVal)
            insertValNode.next = insertValNode
            return insertValNode
        cur = head
        
        # Loop once
        while cur.next != head:
            # Case 2: insert in middle of list
            # 1  -> 3
            #    2
            # cur    cur.next
            if cur.val <= insertVal <= cur.next.val:
                insertValNode = Node(insertVal, cur.next)
                cur.next = insertValNode
                return head
            # Case 3 insertion at edge of list
            #     1  -> 2
            #           cur
            #   0         3
            elif (cur.val > cur.next.val) and (insertVal < cur.next.val or insertVal > cur.val):
                insertValNode = Node(insertVal, cur.next)
                cur.next = insertValNode
                return head
            cur = cur.next
        # Case 4: All nodes are same value
        # 1-> 1 -> 1 -> 1
        # Insert at any position
        insertValNode = Node(insertVal, cur.next)
        cur.next = insertValNode
        return head