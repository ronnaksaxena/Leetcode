class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        '''
        BFS on grid2
        1. inbounds
        2. unvisited
        3. grid1[row][col] == 1 and grid2[row][col] == 1
        
        time: O(rows + cols)
        space: O(rows + cols) for visited set
        '''
        
        rows, cols = len(grid2), len(grid2[0])
        
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        visited = set()
        subIslands = 0
        
        for r in range(rows):
            for c in range(cols):
                
                if (r, c) not in visited and grid2[r][c] == 1:
                    # Start BFS
                    visited.add((r,c))
                    # Potential sub island
                    isSubIsland = True
                    q = collections.deque([(r, c)])
                    while q:
                        curR, curC = q.popleft()
                        # Not a valid subIsland
                        if grid1[curR][curC] != 1:
                            isSubIsland = False
                        for dR, dC in dirs:
                            newR, newC = curR+dR, curC+dC
                            if 0 <= newR < rows and 0 <= newC < cols and (newR, newC) not in visited and grid2[newR][newC] == 1:
                                q.append((newR, newC))
                                visited.add((newR, newC))
                    subIslands += isSubIsland
                                
        return subIslands
                        
                
        
        