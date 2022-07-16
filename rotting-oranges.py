class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        
        rows, cols = len(grid), len(grid[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        q = collections.deque()
        freshOranges = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    freshOranges += 1
        minutes = 0            
        
        while q and freshOranges > 0:
            # Can safely increments minutes here since we check the first level for all rotten oranges
            minutes += 1
            for _ in range(len(q)):
                curR, curC = q.popleft()
                for dR, dC in dirs:
                    newR, newC = curR+dR, curC+dC
                    # ignore if not a fresh orange or OOB
                    if newR < 0 or newC < 0 or newR >= rows or newC >= cols or grid[newR][newC] in [0,2]:
                        continue
                    
                    # Mark as orange found and continue search
                    freshOranges -= 1
                    grid[newR][newC] = 2
                    q.append((newR,newC))
                
                
                            
        return minutes if freshOranges == 0 else -1
                        
                
            
