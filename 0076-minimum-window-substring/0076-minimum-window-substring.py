class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        '''
        s = "ADOBECODEBANC", t = "ABC"
             l
                  r
        shortest = 0,5
        have = 0
        need = 0
        
        tCount = {
        A: 1
        B: 1
        C: 1
        }
        
        window = {}
        '''
        
        if not t:
            return ''
        
        tCount, window = collections.Counter(t), collections.defaultdict(int)
        have, need = 0, len(tCount.keys())
        length = float('inf')
        ptrs = [-1, -1]
        l = 0
        for r in range(len(s)):
            window[s[r]] += 1
            # Found valid freq of char
            if s[r] in tCount and window[s[r]] == tCount[s[r]]:
                have += 1
            
            while have == need:
                # Found smaller substring
                if (r-l+1) < length:
                    ptrs = [l, r]
                    length = r - l + 1
                # update window
                window[s[l]] -= 1
                if window[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1
            
        return s[ptrs[0]:ptrs[1]+1] if ptrs != [-1, -1] else ''
                
            
            
            
            
            
            
        