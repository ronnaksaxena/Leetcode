class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''
        
        res = [0,0]
        resLen = float('inf')
        r, l = 0, 0
        window, tCount = collections.defaultdict(int), collections.Counter(t)
        have, need = 0, len(tCount)
        while r < len(s):
            window[s[r]] += 1
            
            if s[r] in tCount and window[s[r]] == tCount[s[r]]:
                have += 1
            
            while have == need:
                if r-l+1 < resLen:
                    res[0], res[1], resLen = l, r, r-l+1
                
                window[s[l]] -= 1
                if s[l] in tCount and window[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1
            
            r += 1
            
​
        
        return s[res[0]:res[1]+1] if resLen != float('inf') else ''
            
