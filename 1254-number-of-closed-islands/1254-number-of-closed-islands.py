class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        islands = 0
        visited = set()
        def foundIsland(r, c, visited):
            isClosed = True
            visited.add((r,c))
            q = collections.deque([(r,c)])
            while q:
                curR, curC = q.popleft()
                for dR, dC in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    newR, newC = curR+dR, curC+dC
                    if newR < 0 or newR >= rows or newC < 0 or newC >= cols:
                        continue
                    if grid[curR][curC] == 0 and (curR == 0 or curR == rows-1 or curC == 0 or curC == cols-1):
                        isClosed = False
                    if (newR, newC) not in visited and grid[newR][newC] == 0:
                        q.append((newR, newC))
                        visited.add((newR, newC))
            return isClosed
        
        for i in range(1, rows-1):
            for j in range(1, cols-1):
                if grid[i][j] == 0 and (i,j) not in visited and foundIsland(i, j, visited):
                    islands += 1

        return islands
                
        
    