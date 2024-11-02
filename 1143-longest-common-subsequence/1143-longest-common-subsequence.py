class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def dp(i1, i2):
            if i1 == -1 or i2 == -1:
                return 0
            
            if text1[i1] == text2[i2]:
                return 1 + dp(i1-1, i2-1)
            else:
                return max(dp(i1-1, i2), dp(i1, i2-1))

        return dp(len(text1)-1, len(text2)-1)
        