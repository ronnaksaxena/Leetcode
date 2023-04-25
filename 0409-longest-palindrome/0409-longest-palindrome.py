class Solution:
    def longestPalindrome(self, s: str) -> int:
        longest = 0
        letters = collections.Counter(s)
        
        for c in range(ord('A'), ord('z')+1):
            curChar = chr(c)
            if not curChar.isalpha(): continue
            if curChar in letters and letters[curChar] > 1:
                    longest += (letters[curChar] // 2) * 2
        if any(x%2 for x in letters.values()):
            longest += 1
        return longest
        