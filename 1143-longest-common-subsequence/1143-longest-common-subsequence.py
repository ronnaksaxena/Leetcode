class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # i = text 1 length
        # j = text 2 length
        dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        # Base case for empty string already initialized
        # Start at length 1
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    # Chop off both suffixed
                    dp[i][j] = 1  + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]
        