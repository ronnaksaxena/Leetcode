class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        lives = [[-1 for _ in range(cols)] for _ in range(rows)]
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        
        #queue is (row, col, livesLeft, distance)
        q = deque([(0,0,k, 0)])
        
        while q:
            curR, curC, curLives, curDistance = q.popleft()
            
            #if reached end
            if curR == rows-1 and curC == cols-1:
                return curDistance
            
            #if we're at an obstacle decriment lives left
            if grid[curR][curC] == 1:
                curLives -= 1
                #if out of lives quit serching path
                if curLives < 0: continue
            
            for (dR, dC) in dirs:
                newR, newC = curR+dR, curC+dC
                if 0 <= newR < rows and 0 <= newC < cols and curLives > lives[newR][newC]:
                    q.append((newR,newC,curLives, curDistance+1))
                    lives[newR][newC] = curLives
                
            
            
            
            
        return -1
        
