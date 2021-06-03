# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helpMe(iotIdx, left, right):
            
            if left > right: #no subtree
                return None
            
            cur = postorder.pop() #gets last val or root
            idx = iotIdx[cur]
            
            root = TreeNode(cur)
            root.right = helpMe(iotIdx, idx+1, right)
            root.left = helpMe(iotIdx, left, idx-1)
            return root
            
            
            
        iotIdx = {val:idx for idx, val in enumerate(inorder)}
        return helpMe(iotIdx, 0, len(postorder)-1)
