# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        output = []
        to_delete_set = set(to_delete)

        def dfs(node, to_delete_set):
            nonlocal output
            if not node:
                return None
            
            left = dfs(node.left, to_delete_set)
            right = dfs(node.right, to_delete_set)

            # Case 1 current node processed in to_delete_set
            if node.val in to_delete_set:
                if left:
                    output.append(left)
                if right:
                    output.append(right)
                return None

            # Need to update ptrs
            node.left = left
            node.right = right
            return node


        finalRoot = dfs(root, to_delete_set)
        if finalRoot:
            output.append(finalRoot)

        return output
        