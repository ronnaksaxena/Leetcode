class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        DP = [[0 for _ in range(len(word1)+1)] for _ in range(len(word2)+1)]

        for c in range(len(DP[0])):
            DP[0][c] = c

        for r in range(len(DP)):
            DP[r][0] = r

        # word 2
        for i in range(1, len(DP)):
            # word 1
            for j in range(1, len(DP[0])):
                if word1[j-1] == word2[i-1]:
                    DP[i][j] = DP[i-1][j-1]
                else:
                    DP[i][j] = 1 + min(DP[i-1][j-1], DP[i-1][j], DP[i][j-1])

        return DP[-1][-1]


        