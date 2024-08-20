# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:

        def isLeaf(node):
            return not node.left and not node.right

        graph = collections.defaultdict(list)
        q = collections.deque([root])
        leaves = set()
        while q:
            cur = q.popleft()
            if isLeaf(cur):
                leaves.add(cur)
            if cur.left:
                graph[cur].append(cur.left)
                graph[cur.left].append(cur)
                q.append(cur.left)
            if cur.right:
                graph[cur].append(cur.right)
                graph[cur.right].append(cur)
                q.append(cur.right)
        validPairs = set()

        def findValidPairs(rootNode):
            nonlocal validPairs
            q = collections.deque([rootNode])
            visited = set()
            depth = 0
            while q:
                for _ in range(len(q)):
                    cur = q.popleft()
                    if cur in leaves and cur != rootNode:
                        validPairs.add(tuple(sorted([rootNode, cur], key = lambda x: x.val)))
                    for nei in graph[cur]:
                        if nei not in visited:
                            q.append(nei)
                            visited.add(nei)
                depth += 1
                if depth > distance:
                    break
            return


        for leaf in leaves:
             findValidPairs(leaf)
        return len(validPairs)
        