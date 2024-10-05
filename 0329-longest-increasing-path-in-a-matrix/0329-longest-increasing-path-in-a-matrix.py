class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        ROWS, COLS = len(matrix), len(matrix[0])
        memo = [[-1] * COLS for _ in range(ROWS)]  # Initialize memo with -1 (unvisited)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

        def dfs(r, c):
            if memo[r][c] != -1:
                return memo[r][c]
            
            max_path = 1  # The cell itself counts as a path of length 1
            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                if 0 <= newR < ROWS and 0 <= newC < COLS and matrix[newR][newC] > matrix[r][c]:
                    max_path = max(max_path, 1 + dfs(newR, newC))
            
            memo[r][c] = max_path  # Cache the result for future reference
            return memo[r][c]

        maxLengthPath = 0
        for r in range(ROWS):
            for c in range(COLS):
                maxLengthPath = max(maxLengthPath, dfs(r, c))

        return maxLengthPath
