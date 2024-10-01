class Uf:
    def __init__(self, n):
        # index of a node is ROWS * r + c
        self.par = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]

    def find(self, node):
        print(node)
        while self.par[node] != node:
            self.par[node] = self.par[self.par[node]] # path compression
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

    def isConnected(self, n1, n2):
        return self.find(n1) == self.find(n2)

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
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
        ROWS, COLS = m, n
        grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        def getNeighbors(r,c):
            output = []
            dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            for dR, dC in dirs:
                newR, newC = dR+r, dC+c
                if newR in range(ROWS) and newC in range(COLS) and grid[newR][newC] == 1:
                    output.append([newR, newC])
            return output

        count = ROWS * COLS
        uf = Uf(count)
        output = []
        totalIslands = 0

        for r, c in positions:
            if grid[r][c] == 1:
                output.append(totalIslands)
                continue

            grid[r][c] = 1
            totalIslands += 1
            currentNode = COLS * r + c
            for adjR, adjC in getNeighbors(r, c):
                neighborNode = COLS * adjR + adjC
                if uf.union(currentNode, neighborNode):
                    totalIslands -= 1
            output.append(totalIslands)

        return output

            

            

        