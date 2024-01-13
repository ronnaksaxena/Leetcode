class Solution:
    def minSteps(self, s: str, t: str) -> int:
        '''
        - s and t same length
        - non null
        - lowercase english letters
        
        sMap = {char: frequency}
        tMap = {char: frequency}
        
        sMap  = {
        a: 1
        b: 2
        }
        
        tMap = {
            a: 2
            b: 1
        }
        
        changes = 2
        
        loop thorugh char, freq in sMap:
            changes += abs(freq - tMap[char])
        
        return changes
            
        '''
        count = collections.defaultdict(int)
        for i in range(len(s)):
            count[s[i]] += 1
            count[t[i]] -= 1
        return sum(max(0, c) for c in count.values())
            
        