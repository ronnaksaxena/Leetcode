class Solution:
    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        L, R = left, right
        while L >= 0 and R < len(s) and s[L] == s[R]:
            L = L - 1
            R = R + 1
        #return length of palendrome
        return R - L - 1
    
    
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 1: return ""
        start = end = 0
        for i in range(len(s)):
            #loops twice in case palendrome is even
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i+1)
            mlen = max(len1, len2)
            if (end - start) < mlen:
                start = i - (mlen - 1)//2
                end = i + (mlen)//2
        return s[start:end +1]
