class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(matrix), len(matrix[0])
        # Have to switch rxc to cxr since dimensions change
        ans = [[0 for _ in range(ROWS)] for _ in range(COLS)]
        for r in range(ROWS):
            for c in range(COLS):
                ans[c][r] = matrix[r][c]
                
        return ans
        