class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == '1':
                    islands += 1
                    q = collections.deque([(i,j)])
                    visited.add((i,j))
                    while q:
                        curR, curC = q.popleft()
                        
                        for dR, dC in [(-1,0), (1,0), (0, 1), (0, -1)]:
                            newR, newC = curR+dR, curC+dC
                            if 0 <= newR < len(grid) and 0 <= newC < len(grid[0]) and (newR, newC) not in visited and grid[newR][newC] == '1':
                                q.append((newR, newC))
                                visited.add((newR, newC))
        return islands
                        
                
        