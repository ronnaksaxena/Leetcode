class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        '''
        [9,9,4]
        [6,6,8]
        [2,1,1]

        4 0.  [4, 0] => init all elements to 1
        3 2.  [3, 2]
        0 1.  [0, 1]

        [(3, 1), (1, 1), ]
        [(1, 1), (4, 2)]
        [(2, 2)]

        Algo
        init memoization matrix same dimensions as matrix
        maxLenghtPath = 0
        loop throught all elements in matrix
            dfs traversal to update maxLengthPath vars
                - update path
                - loop throught all increasing in bounds neighbors and add to our stack if they yiel a shorter path

        return maxLengthPath

        Time Complexity: O(n^2) where n is all elements in list
        Space: O(n) for memo cache

        '''

        ROWS, COLS = len(matrix), len(matrix[0])
        memo = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        maxLengthPath = 0
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for r in range(ROWS):
            for c in range(COLS):
                if memo[r][c] == 0:
                    stack = [(1, r, c)]
                    while stack:
                        distanceSoFar, curR, curC = stack.pop()
                        if memo[curR][curC] < distanceSoFar:
                            memo[curR][curC] = distanceSoFar
                            maxLengthPath = max(maxLengthPath, distanceSoFar)
                            for dR, dC in dirs:
                                newR, newC = curR + dR, curC + dC
                                if 0 <= newR < ROWS and 0 <= newC < COLS and matrix[curR][curC] < matrix[newR][newC] and memo[newR][newC] < (distanceSoFar+1):
                                    stack.append((distanceSoFar+1, newR, newC))
        
        return maxLengthPath


