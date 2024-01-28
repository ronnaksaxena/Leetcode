# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.cur = root
        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left
        

    def next(self) -> int:
        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left
        self.cur = self.stack.pop()
        nextVal = self.cur.val
        self.cur = self.cur.right
        return nextVal
        

    def hasNext(self) -> bool:
        return self.cur != None or len(self.stack) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
'''
- Assume valid next calls
- Input tree can be null
- Can be duplicate values
- Valid BST

    Idea: In order traversal to get sorted order (least -> greatest)
    - stack iterative in order traversal
    
        7
        /\
       3  15
       /\    /\
            9 20

    stack = [7, 3]
    cur = None
    
    Next(self) => O(1)
    edge case left leaning tree
        while cur: 
            stack push cur
            cur = cur left
        cur = stack pop
        nextVal = cur.val
        cur = cur.right
        return nextVal
    
    hasNext => O(1)
        return cur or stack
       
        
        
        
'''