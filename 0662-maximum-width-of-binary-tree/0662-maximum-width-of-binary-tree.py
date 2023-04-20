# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxWidth = 0
        q = collections.deque([(root, 1)])
        while q:
            # First elem in q is leftmost elem in level
            leftIdx = q[0][1]
            for _ in range(len(q)):
                cur, idx = q.popleft()
                # Need to populate with indices becuase of null nodes children
                maxWidth = max(maxWidth, idx - leftIdx + 1)
                if cur.left:
                    q.append((cur.left, idx * 2))
                if cur.right:
                    q.append((cur.right, idx * 2 + 1))

        
        return maxWidth
        