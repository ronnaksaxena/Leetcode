# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # Egdge case no tree
        if not root:
            return True
        def findDepth(root):
            if not root:
                return 0
            return 1 + max(findDepth(root.left), findDepth(root.right))
        levels = findDepth(root) - 1
        # Num nodes at level i is 2^i
        curLevel = 0
        q = collections.deque([root])
        while q:
            if curLevel == levels - 1:
                # check they are all left leaning
                numNodes = 2 ** curLevel
                if len(q) != numNodes:
                    # Not enough nodes
                    print('Not enough nodes', node.val)
                    return False
                foundRightMost = False
                # Check for left leaning
                for i in range(numNodes):
                    # print(q[i].val, foundRightMost)
                    if foundRightMost:
                        if q[i].left or q[i].right:
                            return False
                    else:
                        if  q[i].right and q[i].left:
                            continue
                        elif not q[i].left and q[i].right:
                            return False
                        else:
                            foundRightMost = True
                    
                # Don't need to check last level
                break
            else:
                numNodes = 2 ** curLevel
                if len(q) != numNodes:
                    # Not enough nodes
                    print('not enough nodes', [n.val for n in q])
                    return False
                for _ in range(numNodes):
                    node = q.popleft()
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                curLevel += 1
            
            
        return True
        