# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        def iot(root):
            return iot(root.left) + [root.val] + iot(root.right) if root else []
        
        def build(nums, l, r):
            if l > r:
                return None
            m = l + (r-l)//2
            node = TreeNode(nums[m])
            node.left = build(nums,l,m-1)
            node.right = build(nums,m+1,r)
            return node
                
                
                
        
        nums = iot(root)
        return build(nums, 0, len(nums)-1)
        
        
