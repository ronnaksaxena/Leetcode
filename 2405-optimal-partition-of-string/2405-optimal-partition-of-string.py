class Solution:
    def partitionString(self, s: str) -> int:
        '''
        "abacaba"
             l
                r
         
         letters = {a}
         parts = 4
        '''
        parts = 1
        l, r = 0, 0
        letters = set()
        while r < len(s):
            if s[r] in letters:
                parts += 1
                l = r
                letters = {s[r]}
            else:
                letters.add(s[r])
            r += 1
        return parts
        