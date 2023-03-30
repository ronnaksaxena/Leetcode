class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        "AABABBA", k = 1
         l
             r

        Map = {
            A: 2
            B: 1
        }
        longest = 1

        if length of window - Most frequent > K:
          change window
          while length of window - Most frequent > K:
            Map[s[l]] -= 1
            l += 1
        '''

        count = collections.defaultdict(int)
        l = 0
        longestSub = 0
        for r in range(len(s)):
          count[s[r]] += 1
          while (r-l+1) - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1
          longestSub = max(longestSub, r - l + 1)
        return longestSub

        