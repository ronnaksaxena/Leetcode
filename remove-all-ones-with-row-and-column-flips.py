class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        r, invR = grid[0], [abs(val-1) for val in grid[0]]
        for row in grid:
            if row != r and row != invR:
                return False
        return True
