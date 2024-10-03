import collections
from typing import List

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        # Distance sum from all houses to each land (0) cell
        distance = [[0] * COLS for _ in range(ROWS)]
        # Reach array to track how many houses can reach each land cell
        reach = [[0] * COLS for _ in range(ROWS)]
        housesCount = 0

        # BFS from each house to calculate the total distance and reach
        def BFS(startRow, startCol):
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            visited = [[False] * COLS for _ in range(ROWS)]
            q = collections.deque([(startRow, startCol, 0)])  # (row, col, distance from house)
            visited[startRow][startCol] = True
            
            while q:
                r, c, dist = q.popleft()
                
                # Visit all 4 directions
                for dr, dc in dirs:
                    newR, newC = r + dr, c + dc
                    if 0 <= newR < ROWS and 0 <= newC < COLS and grid[newR][newC] == 0 and not visited[newR][newC]:
                        visited[newR][newC] = True
                        distance[newR][newC] += dist + 1  # Add the distance from the house
                        reach[newR][newC] += 1  # Increment the reach count for this cell
                        q.append((newR, newC, dist + 1))

        # Count the number of houses and perform BFS from each house
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    housesCount += 1
                    BFS(r, c)

        # Find the land cell with the minimum total distance that can reach all houses
        minDistance = float('inf')
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0 and reach[r][c] == housesCount:  # Only consider cells reachable by all houses
                    minDistance = min(minDistance, distance[r][c])

        return minDistance if minDistance != float('inf') else -1
