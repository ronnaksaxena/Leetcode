class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        
        for i in range(rows):
            for j in range(cols):
                if i == 0 and j == 0:
                    continue
                # Can't make a path from top cell
                if i == 0:
                    grid[i][j] += grid[i][j-1]
                # Can't make a path from right
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        return grid[-1][-1]
                    
                
        
