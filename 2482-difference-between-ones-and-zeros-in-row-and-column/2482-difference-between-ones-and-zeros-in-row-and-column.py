class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        '''
        rows = {ith row: [zeroesCount, onesCount]}
        cols = {jth col: [zeroesCount, onesCount]}
        
        1. iterate and populate map
        2. init diff matrix
        3. iterate througha and compute diff
        
        '''
        ROWS, COLS = len(grid), len(grid[0])
        rows = {0: [0 for _ in range(ROWS)],
               1: [0 for _ in range(ROWS)]}
        
        cols = {0: [0 for _ in range(COLS)],
               1: [0 for _ in range(COLS)]}
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    rows[1][i] += 1
                    cols[1][j] += 1
                else:
                    rows[0][i] += 1
                    cols[0][j] += 1
        diff = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        for i in range(ROWS):
            for j in range(COLS):
                diff[i][j] = rows[1][i] + cols[1][j] - rows[0][i] - cols[0][j]
        return diff
                    
        