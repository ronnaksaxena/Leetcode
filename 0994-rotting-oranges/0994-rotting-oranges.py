class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        input: 2D array
        output: int

        Qs:
        -Valid input
        - Not empty list
        - all rotten then 0

        Intuition: BFS approach
        - At each depth of traversal increment how much time has passed
        - F <- F <- R
        - No path from a rotten orange to a fresh orange, return -1
            - count remaining fresh oranges

        Algo:
        - Iterate through all cells
            - count fresh oranges
            - put all rotten oranges in q
        - init timePassed = 0
        - BFS using our q
        - while q and remainingFreshOranges > 0:
            - loop through lenght of q:
                pop rotten tomato from front of q
                loop through its 4 neighbors:
                    if fresh orange:
                        dec remainingFreshOrange
                        enquee this new rotten orange
            inc timePassed
        - return timePassed if remainingFreshOranges is > 0 otherwise -1

        Time: O(N)
        Space: O(N) for q
        
        '''

        freshOranges = 0
        q = collections.deque()
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    freshOranges += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
        
        timePassed = 0
        dirs = [[-1,0], [1,0], [0, 1], [0, -1]]
        while q and freshOranges > 0:
            for _ in range(len(q)):
                curR, curC = q.popleft()
                for dR, dC in dirs:
                    newR, newC = curR + dR, curC + dC
                    if 0 <= newR < rows and 0 <= newC < cols and grid[newR][newC] == 1:
                        freshOranges -= 1
                        q.append((newR, newC))
                        grid[newR][newC] = 2
            timePassed += 1
        
        return timePassed if freshOranges == 0 else -1

