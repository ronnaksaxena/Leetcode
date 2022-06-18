class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        maxArea = 0
        visited = set()
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #found island
                if grid[i][j] == 1 and (i,j) not in visited:
                    
                    #conduct a DFS on adjacent island coordinates
                    curArea = 0
                    stack = [(i,j)]
                    visited.add((i,j))
                    while stack:
                        curR, curC = stack.pop()
                        #traversed another land coordinate
                        curArea += 1
                        for dr,dc in dirs:
                            newR, newC = curR + dr, curC + dc
                            if 0 <= newR < len(grid) and 0 <= newC < len(grid[0]) and (newR,newC) not in visited and grid[newR][newC]:
                                visited.add((newR,newC))
                                stack.append((newR,newC))
                                
                    maxArea = max(maxArea, curArea)
                    
        
        return maxArea
                    
                    
        
