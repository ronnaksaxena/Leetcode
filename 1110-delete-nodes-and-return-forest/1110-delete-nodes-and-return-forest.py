# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        to_delete_set = set(to_delete)
        output = []
        def dfs(node):
            nonlocal to_delete_set, output
            if not node:
                return
            left = dfs(node.left)
            right = dfs(node.right)

            if node.val in to_delete_set:
                if left:
                    output.append(left)
                if right:
                    output.append(right)
                del node
                return None
            else:
                node.left = left
                node.right = right
                return node

        new_root = dfs(root)
        if new_root:
            output.append(new_root)
        return output

        
        