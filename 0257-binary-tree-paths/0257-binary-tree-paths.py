# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        output = []
        def dfs(node, curPath = []):
            nonlocal output
            if not node.left and not node.right:
                path = '->'.join(curPath) + '->' + str(node.val) if curPath else str(node.val)
                output.append(path)
                return
            curPath.append(str(node.val))
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            curPath.pop()

        dfs(root)
        return output


        