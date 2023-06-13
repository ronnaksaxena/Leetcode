class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        output = 0
        for r in range(n):
            for c in range(n):
                foundMatch = True
                for i in range(n):
                    if grid[i][c] != grid[r][i]:
                        foundMatch = False
                        break
                output += foundMatch
                        
        return output
        