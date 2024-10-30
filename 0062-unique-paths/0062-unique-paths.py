class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        r 1 1 1
        1 2 3 4
        1 3 6  10

        - can only move down or right
            - can only reach current location from left or up

        '''

        DP = [[0 for _ in range(n)] for _ in range(m)]
        # Top row has 1 unique path
        for c in range(n):
            DP[0][c] = 1
        # Left col has 1 unique path
        for r in range(m):
            DP[r][0] = 1

        for r in range(1, m):
            for c in range(1, n):
                DP[r][c] = DP[r-1][c] + DP[r][c-1]

        return DP[-1][-1]
        