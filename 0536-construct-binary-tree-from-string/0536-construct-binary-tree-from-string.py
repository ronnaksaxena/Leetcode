# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        '''
        - number can be negative or mulitple digits
        - valid number
        
            4
        /       \
        2       6
        /\      /
        3 1     5
        
        "4(2(3)(1))(6(5))"
        
        '''
        '''
        return (int, next index)
        '''
        def getNumber(i):
            num = 0
            isNeg = False
            if i < len(s) and s[i] == '-':
                isNeg = True
                i += 1
            while i < len(s) and s[i].isdigit():
                num = (num*10) + int(s[i])
                i += 1
            return (-1 * num if isNeg else num), i
            
            
        '''
        return (node, index)
        '''
        def buildTree(i):
            if i == len(s):
                return None, i
            # Create node with this current value
            nodeVal, i = getNumber(i)
            root = TreeNode(nodeVal)
            # Check if there is a left subtree to build
            if i < len(s) and s[i] == '(':
                root.left, i = buildTree(i+1)
            # Check if there is a right subtree to build
            if i < len(s) and s[i] == '(':
                root.right, i = buildTree(i+1)
            # Avoid ignore the )
            return root, i + 1 if i < len(s) and s[i] == ')' else i
        return buildTree(0)[0]
            
            
            
            
            
            
            