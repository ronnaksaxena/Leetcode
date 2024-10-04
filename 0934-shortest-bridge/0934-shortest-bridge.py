class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        '''
        [[1,1,1,1,1]
        [1,0,0,0,1]
        [1,0,1,0,1]
        [1,0,0,0,1]
        [1,1,1,1,1]]

        maintain set of coords in island1
        another set of coords in island2

        toss all elements in island2 into q
        depth = 0
        BFS:
            loop thorught lenghth of q
                - check if current element in island1:
                    return depth -1
                loop through 4 neighbors of current coordinate
                    - if not in island2: add to island2 and q

        Time: O(N) where N is total elements in grid
        Space: O(N) for q

        '''
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(-1,0), (1, 0), (0, -1), (0, 1)]
        def initIsland(r, c, visited):
            visited.add((r,c))
            q = collections.deque([(r,c)])
            while q:
                curR, curC = q.popleft()
                for dR, dC in dirs:
                    newR, newC = curR+dR, curC+dC
                    if 0 <= newR < ROWS and 0 <= newC < COLS and grid[newR][newC] == 1 and (newR, newC) not in visited:
                        visited.add((newR, newC))
                        q.append((newR, newC))
            return
            

        island1 = set()
        island2 = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    if len(island1) == 0:
                        # init island1
                        initIsland(r, c, island1)
                    elif (r,c) not in island1:
                        # init island2
                        initIsland(r, c, island2)
                        break
            if len(island2) >= 1:
                break
        # print(f'island1 {island1}')
        # print(f'island2 {island2}')
        # BFS on island 2
        q = collections.deque([coord for coord in island2])
        depth = 0
        while q:
            for _ in range(len(q)):
                curR, curC = q.popleft()
                if (curR, curC) in island1:
                    return depth -1
                for dR, dC in dirs:
                    newR, newC = curR+dR, curC+dC
                    if 0 <= newR <= ROWS and 0 <= newC <= COLS and (newR,newC) not in island2:
                        q.append((newR, newC))
                        island2.add((newR, newC))
            depth += 1
        return -1

                
        