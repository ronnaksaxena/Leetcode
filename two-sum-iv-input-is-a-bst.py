# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        BFS = []
        q = []
        q.append(root)
        while q:
            cur = q.pop(0)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
            BFS.append(cur.val)
        
        BFS.sort()
        print(BFS)
        for i in range(len(BFS)):
            for j in range(i):
                if BFS[i]+BFS[j]==k:
                    return True
                if BFS[i]+BFS[j]>k:
                    break
        return False
