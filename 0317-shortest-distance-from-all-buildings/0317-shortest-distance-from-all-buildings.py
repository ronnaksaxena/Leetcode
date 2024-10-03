import collections
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        '''
        Clarification questions:
        - input: 2d int Arr, output: int
        - if tie return ans
        - return -1 if no 0s, garunteed a builiding
        - valid inputs? yes

        edge cases:
            - no 0s to build house
            - no path to any building
            [[0, 2, 1]]

        Algo:
        1. iterate throught grid and store all coordinates of 0s in a list
            - if no 0s in grid: no solution
        2. init ans = -inf => shortest path
        3. Try a BFS on all 0 starting points (potentially djisktra or A*)
            - see if you can reach all 1s before search terminates
            - if not no solution
            - update ans = min(ans, distance to every house)
        4. Return ans


        N = m(ROWS) * n(COLS)

        O(N^2) => iterating thorugh all 0 coordinates and conducting a BFS traversal
        Space: O(N) for list to store potential land plots and visited set


        '''
        ROWS, COLS = len(grid), len(grid[0])
        def BFS(startRow, startCol, visited, housesCount):
            '''
            - input: row, col of house, visited set
            - output: sum of manhattan distances to house
            distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|
            - return float('inf') if can't reach all houses
            '''
            visited.add((startRow,startCol))
            q = collections.deque([(startRow,startCol)])
            housesFound = 0
            totalDistance = 0
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            while q and housesFound < housesCount:
                curR, curC = q.popleft()
                if grid[curR][curC] == 1:
                    housesFound += 1
                    totalDistance += (abs(startRow-curR) + abs(startCol-curC))
                    continue
                for dR, dC in dirs:
                    newR, newC = curR + dR, curC + dC
                    if 0 <= newR < ROWS and 0 <= newC < COLS and grid[newR][newC] != 2 and (newR, newC) not in visited:
                        visited.add((newR, newC))
                        q.append((newR, newC))
            return totalDistance if housesFound == housesCount else float('inf')
                
                

        
        houseCandidates = []
        minDistance = float('inf')
        housesCount = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    houseCandidates.append((r,c))
                elif grid[r][c] == 1:
                    housesCount += 1
        
        for r,c in houseCandidates:
            visited = set()
            minDistance = min(minDistance, BFS(r,c, visited, housesCount))

        return minDistance if minDistance != float('inf') else -1
        
