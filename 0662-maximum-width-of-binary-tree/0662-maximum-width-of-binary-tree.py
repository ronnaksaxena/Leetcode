# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxWidth = 0
        q = collections.deque([(root, 0)])
        while q:
            leftIdx = q[0][1]
            for _ in range(len(q)):
                cur, idx = q.popleft()
                maxWidth = max(maxWidth, idx - leftIdx + 1)
                if cur.left:
                    q.append((cur.left, idx * 2))
                if cur.right:
                    q.append((cur.right, idx * 2 + 1))

        
        return maxWidth
        