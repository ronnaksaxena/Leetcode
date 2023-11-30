class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if r == 0 and c == 0: continue
                elif r == 0:
                    # Don't check up
                    grid[r][c] += grid[r][c-1]
                elif c == 0:
                    # Dont check right
                    grid[r][c] += grid[r-1][c]
                else:
                    # Check both
                    grid[r][c] += min(grid[r-1][c], grid[r][c-1])
        
        # Min sum should be bottom right value
        return grid[-1][-1]
            
        