# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = []
        q.append(root)
        #if odd get left->right level order
        #if even get right->left level order
        levelNum = 1
        while q:
            level = []
            for i in range(len(q)):
                cur = q.pop()
                if cur.left:
                    q.insert(0, cur.left)
                if cur.right:
                    q.insert(0, cur.right)
                level.append(cur.val)
            if levelNum%2==1:
                res.append(level)
                levelNum += 1
            else:
                res.append(reversed(level))
                levelNum += 1
        return res
        
