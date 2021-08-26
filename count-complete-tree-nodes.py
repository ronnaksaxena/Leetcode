# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        L, R = 0, 0
        LPtr = RPtr = root
        while LPtr and RPtr: #check if subtree is perfect or not
            LPtr, RPtr, L, R = LPtr.left, RPtr.right, L+1, R+1
        
        if LPtr == RPtr: #found perfect subtree so num of nodes is 2^height-1
            return 2**L-1
        else: #keep looking for perfect subtree
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
