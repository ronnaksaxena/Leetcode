# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val
        while root:
            if abs(root.val-target) < abs(closest-target):
                closest = root.val
            elif abs(root.val-target) == abs(closest-target):
                closest = min(root.val, closest)
            root = root.left if target < root.val else root.right
        return closest
        