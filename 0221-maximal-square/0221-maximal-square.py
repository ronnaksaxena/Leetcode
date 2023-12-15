class Solution:
    # Changes so that board is ints !!
    def maximalSquare(self, matrix: List[List[int]]) -> int:
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for rowIdx, row in enumerate(matrix):
            for colIdx, num in enumerate(row):
                if (rowIdx == 0 or colIdx == 0) and num == '1':
                    dp[rowIdx][colIdx] = 1
                elif num == '1':
                    dp[rowIdx][colIdx] = min(dp[rowIdx-1][colIdx], dp[rowIdx][colIdx-1], dp[rowIdx-1][colIdx-1]) + 1
        ans = max(max(x) for x in dp)
        return ans **2
                
        
        