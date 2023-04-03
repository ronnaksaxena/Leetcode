# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        preorder = [3,9,20,15,7]
        inorder = [9,3,15,20,7]
        
        3 dfs(0, 4)
     /.   \
    9dfs(0, 0) 20 dfs(2, 4)
 /.   \        / \
 None None   15 dfs(2,2)
        
        '''
        
        def dfs(left, right):
            if left > right:
                return None
            cur = TreeNode(preorder.pop(0))
            idx = iot[cur.val]
            cur.left = dfs(left, idx-1)
            cur.right = dfs(idx+1, right)
            return cur
        
        iot = {v: i for i, v in enumerate(inorder)}
        return dfs(0, len(inorder)-1)
        