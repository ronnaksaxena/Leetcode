class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r, maxLen = 0,0,0
        map = collections.defaultdict(int)
        
        while r < len(s):
            
            map[s[r]] += 1
            
            mostFreq = max(map, key=map.get)
            numReplaces = (r-l+1) - map[mostFreq]
            
            if numReplaces <= k:
                maxLen = max(maxLen, r-l+1)
            else:
                while numReplaces > k:
                    map[s[l]] -= 1
                    l += 1
                    mostFreq = max(map, key=map.get)
                    numReplaces = (r-l+1) - map[mostFreq]
            r += 1
            
        return maxLen
