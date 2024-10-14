class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def dp(i1, i2):
            if i1 == -1:
                return i2 + 1
            if i2 == -1:
                return i1 + 1
            
            if word1[i1] == word2[i2]:
                return dp(i1-1, i2-1)

            return 1 + min(dp(i1-1,i2-1), dp(i1-1, i2), dp(i1, i2-1))

        return dp(len(word1)-1, len(word2)-1)


        