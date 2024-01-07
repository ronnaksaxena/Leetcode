# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        node = self.stack.pop()
        value = node.val
        node = node.right
        while node:
            self.stack.append(node)
            node = node.left
        return value
        

    def hasNext(self) -> bool:
        return len(self.stack) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

'''
        7
    /       \
    3       15
        /       \
        9       20
        
        
    self.stack = [20]
    
    node = stack.pop()
    value = self.node.val
    
    node = node.right
    while node:
        stack.append(node)
        node = node.left
    
    3 7 9 15
    
    initalize adding left children to stack
    next by using algo
    hasNext == if stack

'''