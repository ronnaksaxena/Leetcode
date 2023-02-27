"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        '''
        Notice:
        In order to be a valid quadtree, grid must be an even square
        Need to only keep track of top right position and length
        
        1. Recrusively build the tree considering the grid parameters
            a check if its a leaf
            b divide grid into 4 parts and do recurisve call on each part
            c return root of QT
        
        Time: O(N) elemnts in grid
        Space: O(h) h is height of tree
        '''
        def isLeaf(grid, x, y, length):
            # 1 square grid
            if length == 1:
                return True
            for r in range(y, y + length):
                for c in range(x, x + length):
                    if grid[r][c] != grid[y][x]:
                        return False
            return True
        # y is row, x is col of top right
        def buildTree(grid, x, y, length):
            if isLeaf(grid, x, y, length):
                return Node(grid[y][x], True)
            root = Node(random.choice([0,1]), False)
            root.topLeft = buildTree(grid, x, y, length // 2)
            root.topRight = buildTree(grid, x + (length//2), y, length // 2)
            root.bottomLeft = buildTree(grid, x, y + (length//2), length // 2)
            root.bottomRight = buildTree(grid, x + (length // 2), y + (length//2), length // 2)
            
            return root
        
        return buildTree(grid, 0, 0, len(grid))
            
            
            
            
        