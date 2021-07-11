class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s) <= 2:
            return len(s)
        
        L, maxLen = 0,0
        
        lastOccur = collections.defaultdict()
        for i in range(len(s)):
            lastOccur[s[i]] = i
            if len(lastOccur) > 2:
                poppedChar = min(lastOccur, key=lastOccur.get)
                L = lastOccur[poppedChar]+1
                lastOccur.pop(poppedChar)
            else:
                maxLen = max(maxLen, i-L+1)
                
        
        return maxLen
