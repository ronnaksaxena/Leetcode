class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
            
        
        
        if not grid:
            return 0
        islands = 0
        
        m = len(grid)
        n = len(grid[0])
        
        def DFS(grid, row, col):
            if row < 0 or row >= m:
                return
            if col < 0 or col >= n:
                return
            if grid[row][col] == '0':
                return
            grid[row][col] = '0'
            DFS(grid, row-1, col)
            DFS(grid, row+1, col)
            DFS(grid, row, col-1)
            DFS(grid, row, col+1)
            return
        
