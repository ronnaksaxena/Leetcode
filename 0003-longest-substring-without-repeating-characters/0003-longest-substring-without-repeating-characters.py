class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniqueChars = collections.defaultdict(int) # char: index
        longest = 0
        l = 0
        for r in range(len(s)):
            if uniqueChars.get(s[r], -1) >= l:
                l = uniqueChars[s[r]] + 1

            uniqueChars[s[r]] = r
            longest = max(longest, r-l+1)

        return longest

        