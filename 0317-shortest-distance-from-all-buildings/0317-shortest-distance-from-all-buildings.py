class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        '''
        input: 2d arr int
        output: sum of distances to all builidngs
        - values can only be 0, 1, 2
        - 4 directional traversal
        - distance = |x1 - x2| + |y1 - y2| => need to take obstacles into account
        - no memory constaints on size of matrix
        - cannot pass through buildings


        EDGE CASE:
        - cant reach all building => return -1
        [[0, 2, 1]]

        IDEA 1: BFS
        - BFS on all 0s and find coordinate with min sum of distance to all 1s
            - if can't reach all 1s from any coordinate => terminate early

        [1, 1000000 * 0 =>]
        100000
        |
        v
        0

        0 0 2 0 0
        0 0 2 1 0
        2 2 2 1 0

        Algo:
        - housesReachedMap = {(x,y): # of houses reaach}
        - distancesMap = {(x,y): sum of distances to each house}
        - houseCount => incr for each 1

        answer is 0 coordinate that has min distance and reaches all houses

        - Do BFS on all 1's
            - populate the maps of neihgboring 0s with distance from that house
        
        Time: (elements in matrix * number of houses)
        Space: O(elements in matrix) for 2 maps and visited set

        '''
        # Only store coordinates of 0s as keys
        housesReached = collections.defaultdict(int) # {(x,y): count}
        distanceToHouses = collections.defaultdict(int) # {(x, y): distnace from each house}
        ROWS, COLS = len(grid), len(grid[0])

        def BFS(startRow, startCol):
            # populate maps
            visited = {(startRow, startCol)}
            q = collections.deque([(startRow, startCol)])
            dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            curDistance = 0
            while q:
                for _ in range(len(q)):
                    curR, curC = q.popleft()
                    if grid[curR][curC] == 0:
                        housesReached[(curR, curC)] += 1
                        # Need to take obstacles into account
                        distanceToHouses[(curR, curC)] += curDistance
                    for dR, dC in dirs:
                        newR, newC = curR+dR, curC+dC
                        if 0 <= newR < ROWS and 0 <= newC < COLS and (newR, newC) not in visited and grid[newR][newC] == 0:
                            q.append((newR, newC))
                            visited.add((newR, newC))
                curDistance += 1

        
        housesCount = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    housesCount += 1
                    BFS(r, c)
        minDistance = float('inf')
        # print(f'distances {distanceToHouses}')
        # print(f'hosues reached {housesReached}')

        for coord, d in distanceToHouses.items():
            if housesReached[coord] == housesCount:
                minDistance = min(minDistance, d)

        return minDistance if minDistance != float('inf') else -1


        