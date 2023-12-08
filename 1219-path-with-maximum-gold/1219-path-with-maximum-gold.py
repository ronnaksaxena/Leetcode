class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        def findNeighbors(r,c):
            nei = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            neighbors = []
            for dR, dC in nei:
                newR, newC = r+dR, c+dC
                if 0 <= newR < ROWS and 0 <= newC < COLS and grid[newR][newC] not in [0, '#']:
                    neighbors.append((newR, newC))
            return neighbors
        def backtrack(r, c):
            oldVal = grid[r][c]
            grid[r][c] = '#'
            neighbors = findNeighbors(r,c)
            maxNeighbor = 0
            for nR, nC in neighbors:
                maxNeighbor = max(maxNeighbor, backtrack(nR, nC))
            grid[r][c] = oldVal
            return oldVal + maxNeighbor
                
        maxGold = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] > 0:
                    maxGold = max(maxGold, backtrack(r,c))
        return maxGold
                        
                
        
        