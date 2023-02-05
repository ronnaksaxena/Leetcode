class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
        s = "cbaebabacd"
             l
                r
        p = "abc"
        {
        a: 0
        b: 1
        c: 1
        }
        output = [0, 6]
        Time: O(n + m) where n == len(s) and m == len(p)
        Space: O(m) where m == len(p)
        '''
        # populate letters count
        letters = {chr(i): 0 for i in range(ord('a'), ord('z')+1)}
        for c in p:
            letters[c] += 1
        l, r = 0, 0
        output = []
        while r < len(s):
            if letters[s[r]] > 0:
                letters[s[r]] -= 1
                # Found anagram
                if sum(letters.values()) == 0:
                    output.append(l)
                r += 1
            elif l < r:
                letters[s[l]] += 1
                l += 1
            else:
                l += 1
                r += 1
        return output
                    
                    
        