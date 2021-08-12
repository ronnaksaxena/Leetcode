class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix: return 0
        m, n, ans = len(matrix), len(matrix[0]), 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:    
                    if i==0 or j==0:
                        ans += 1
                    else:
                        matrix[i][j] = min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1])+1
                        ans += matrix[i][j]
        return ans
