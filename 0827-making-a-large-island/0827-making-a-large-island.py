class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        '''
        - grid wont be null
        - at least 1x1
        
        2 0 0
        2 0 3
        0 0 3
        
        island1 = 2
        island2 = 2
        
        islandAreas = {islandIndex (2-indexed): area}
        maxArea = maxIslandFound
        {2: 2,
        3: 2}
        1. Iterate thorught grid and if cell == 1:
            unvisited
            DFS setting all components to index of island
            islandAreas[islandIndex] = islandArea
            updateArea # Edge case that all elements are 1
        2. Iterate through matrix second time
            -if cell is 0
            - calculate island it could yield by changing to 1
            - checking all neighbors for unique islandneights
            - 1 + sum(island neighbor areas)
            - update maxArea
            
        '''
        # def printGrid():
        #     for r in grid:
        #         print(r)
        
        islandAreas = {}
        islandIndex = 2
        maxArea = 0
        directions = [(-1,0), (1,0), (0, -1), (0, 1)]
        # Calc all existing island area
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    # DFS on island
                    area = 0
                    stack = [(r,c)]
                    while stack:
                        curR, curC = stack.pop()
                        if grid[curR][curC] != islandIndex:
                            # Marking as visited
                            grid[curR][curC] = islandIndex
                            area += 1
                            for dR, dC in directions:
                                newR, newC = curR+dR, curC+dC
                                if 0 <= newR < len(grid) and 0 <= newC < len(grid[0]) and grid[newR][newC] == 1:
                                    stack.append((newR, newC))
                    # Update areas
                    islandAreas[islandIndex] = area
                    maxArea = max(area, maxArea)
                    islandIndex += 1
        # printGrid()
        # print(islandAreas)
        # Find best 0 to change
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    neighbors = set()
                    for dR, dC in directions:
                        newR, newC = r+dR, c+dC
                        if 0 <= newR < len(grid) and 0 <= newC < len(grid[0]) and grid[newR][newC] >= 2:
                            neighbors.add(grid[newR][newC])
                    area = 1 + sum(islandAreas[nei] for nei in neighbors)
                    maxArea = max(maxArea, area)
                    
        return maxArea
        
        
        
        
        
        
        
        
        
        
        
        