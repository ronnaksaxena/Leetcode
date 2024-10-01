'''
Qs:
- m and n at least 1
- positions are valid inputs
- output 1d arr
- no duplicates in positions
1 1 1
1 0 1 0
1 1 0 1
0 1 0

- if no neighbors are 1s: totalIslands += 1
- if only 1 neihgbor is 1: totalIslands doesn't change
- if >= 2 neihgbors are 1: totalIslands -= (neighbors - 1)

edge case: neighbor out of bounds

Algo:
    1. init uf, output arr, grid
    2. loop through positions
        ingore if coord is already 1
        see how many neighbors form new islands
        union to all valid neighbors and count how many are connected
        decriment totalIslands by (existingConnections -1)
    3. reutrn output
'''
import collections
from typing import List

class Uf:
    def __init__(self, n):
        # Each node is initially its own parent (root of its component)
        self.par = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]

    def find(self, node):
        while self.par[node] != node:
            self.par[node] = self.par[self.par[node]]  # Path compression
            node = self.par[node]
        return node
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False  # No union needed, they are already in the same component
        # Union by rank
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.rank[p1] += 1
        return True  # Return True only if a union occurred (i.e., two different components merged)

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        ROWS, COLS = m, n
        grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

        def getNeighbors(r, c):
            # Get valid neighbors that are already land (i.e., grid[r][c] == 1)
            neighbors = []
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                if 0 <= newR < ROWS and 0 <= newC < COLS and grid[newR][newC] == 1:
                    neighbors.append((newR, newC))
            return neighbors

        uf = Uf(ROWS * COLS)  # Initialize union-find data structure
        output = []
        totalIslands = 0  # Track the total number of islands

        for r, c in positions:
            if grid[r][c] == 1:  # If land is already present, no need to add it
                output.append(totalIslands)
                continue

            grid[r][c] = 1  # Mark the current cell as land
            currentNode = r * COLS + c  # Calculate the 1D index of the current cell
            totalIslands += 1  # Assume adding this land creates a new island

            # Check all valid neighbors
            for adjR, adjC in getNeighbors(r, c):
                neighborNode = adjR * COLS + adjC
                # If the neighbor is not already in the same island (disjoint), merge them
                if uf.union(currentNode, neighborNode):
                    totalIslands -= 1  # Merge reduces the number of islands

            output.append(totalIslands)  # Add the current number of islands after this step

        return output
