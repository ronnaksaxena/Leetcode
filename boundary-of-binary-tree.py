# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        
        
        if not root:
            return []
​
        res = [root.val]
        left_boundary = self.find_left_boundary(root.left)
        right_boundary = self.find_right_boundary(root.right)
        leaves = []
        if root.left or root.right:
            self.find_leaves(root, leaves)
​
        res += left_boundary + leaves + right_boundary
        return res
​
    def is_leaf(self, root):
        return not root.left and not root.right
​
    def find_left_boundary(self, root):
        node, parent = root, root
        res = []
        while node and not self.is_leaf(node):
            res.append(node.val)
            if node.left:
                node = node.left
            else:
                node = node.right
        return res
​
    def find_right_boundary(self, root):
        node, parent = root, root
        res = []
        while node and not self.is_leaf(node):
            res.append(node.val)
            if node.right:
                node = node.right
            else:
                node = node.left
​
        return res[::-1]
​
    def find_leaves(self, root, res):
        if self.is_leaf(root):
            res.append(root.val)
​
        if root.left:
