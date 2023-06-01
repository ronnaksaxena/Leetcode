class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        goal = (len(grid)-1, len(grid[0])-1)
        def getDistanceToEnd(row, col):
            return abs(goal[0]-row) + abs(goal[-1]-col)
        
        neighbors = [(-1,-1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        # Edge case if top left is 1
        if grid[0][0] == 1:
            return -1
        # Else run A* search
        q = collections.deque([(getDistanceToEnd(0,0), 1, 0, 0)]) # h(x), length r, c
        visited = {(0,0)}
        while q:
            _, length, r, c = q.popleft()
            if (r,c) == goal:
                return length
            for dR, dC in neighbors:
                newR, newC = r+dR, c+dC
                if (newR, newC) not in visited and 0 <= newR < len(grid) and 0 <= newC < len(grid[0]) and grid[newR][newC] == 0:
                    hx = length + getDistanceToEnd(newR, newC) + 1 # +1 for new spot traversed
                    q.append((hx, length+1, newR, newC))
                    visited.add((newR, newC))
                    
        # Can't reach end
        return -1
        