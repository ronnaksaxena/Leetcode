class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        # Cache best path found
        mostLives = [[float('-inf') for _ in range(cols)] for _ in range(rows)]
        
        target = (rows-1, cols-1)
        visited = {(0,0, k)}
        q = collections.deque([(0,0, k)]) #(row, col, livesLeft)
        dirs = [[-1, 0], [1, 0], [0, -1], [0,1]]
        steps = 0
        while q:
            
            for _ in range(len(q)):
                curRow, curCol, curLives = q.popleft()
                
                if (curRow, curCol) == target:
                    return steps
                # Have ot remove obstacles
                if grid[curRow][curCol] == 1:
                    curLives -= 1
                # Out of lives :(
                if curLives < 0:
                    continue
                if mostLives[curRow][curCol] > curLives:
                    continue # This path sucks
                else:
                    mostLives[curRow][curCol] = curLives
                
                for dR, dC in dirs:
                    newR, newC = curRow+dR, curCol+dC
                    if (newR, newC, curLives) not in visited and 0 <= newR < rows and 0 <= newC < cols:
                        q.append((newR, newC, curLives))
                        visited.add((newR, newC, curLives))
                        
            steps += 1
        # no possible path
        return -1
                
        
        
        