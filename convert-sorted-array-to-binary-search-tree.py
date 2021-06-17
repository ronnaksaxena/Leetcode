# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helpBaby(left, right):
            if left > right:
                return None
            
            idx = (right+left)//2
            r = TreeNode(nums[idx])
            r.left = helpBaby(left, idx-1)
            r.right = helpBaby(idx+1, right)
            return r
        
        return helpBaby(0, len(nums)-1)
