class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        start, maxLen = 0, 0
        map = collections.defaultdict()
        
        for i in range(len(s)):
            if s[i] not in map:
                if len(map) == k:
                    charToDelete = min(map, key=map.get)
                    delIdx = map[charToDelete]
                    map.pop(charToDelete)
                    start = delIdx + 1
            map[s[i]] = i
            
            maxLen = max(maxLen, i-start+1)
        
        return maxLen
