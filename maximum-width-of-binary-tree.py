# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = deque([(root,1)])
        width = 0
        while q:
            _,left = q[0]
            _,right = q[-1]
            width = max(width,right-left+1)
            nextLev = deque()
            while q:
                node,idx = q.popleft()
                if node.left:
                    nextLev.append((node.left,idx*2))
                if node.right:
                    nextLev.append((node.right,idx*2+1))
            q = nextLev
        return width
