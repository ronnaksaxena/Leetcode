# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        cnt = collections.defaultdict(int)
        def dfs(node):
            nonlocal cnt
            if not node:
                return
            cnt[node.val] += 1
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        maxFreq = max(cnt.values())
        return [val for val, freq in cnt.items() if freq == maxFreq]
        