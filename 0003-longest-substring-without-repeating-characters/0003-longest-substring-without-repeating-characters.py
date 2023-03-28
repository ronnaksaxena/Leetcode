class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        letters = {}
        longestSub = 0
        for r in range(len(s)):
            if s[r] in letters.keys():
                l = max(l, letters[s[r]] + 1)
            letters[s[r]] = r
            longestSub = max(longestSub, r - l + 1)
            
        return longestSub
        