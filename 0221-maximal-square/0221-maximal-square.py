class Solution:
    # Changes so that board is ints !!
    def maximalSquare(self, matrix: List[List[int]]) -> int:
        maxSide = 0
        for rowIdx, row in enumerate(matrix):
            for colIdx, num in enumerate(row):
                matrix[rowIdx][colIdx] = int(matrix[rowIdx][colIdx])
                if (rowIdx == 0 or colIdx == 0) and num == '1':
                    maxSide = max(maxSide, 1)
                elif num == '1':
                    matrix[rowIdx][colIdx] = min(matrix[rowIdx-1][colIdx], matrix[rowIdx][colIdx-1], matrix[rowIdx-1][colIdx-1]) + 1
                    maxSide = max(maxSide, matrix[rowIdx][colIdx])
        return maxSide ** 2
                
        
        