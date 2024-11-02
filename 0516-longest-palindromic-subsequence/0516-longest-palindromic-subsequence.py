class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        @cache
        def dp(l, r):
            if l == r:
                return 1
            if (l+1) == r:
                return 2 if s[l] == s[r] else 1

            if s[l] == s[r]:
                return 2 + dp(l+1, r-1)
            else:
                return max(dp(l+1, r), dp(l, r-1))

        return dp(0, len(s)-1)
            
        