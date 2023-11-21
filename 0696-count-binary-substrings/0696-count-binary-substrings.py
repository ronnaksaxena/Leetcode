class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        def countSubs(l, r):
            lChar = s[l]
            rChar = s[r]
            if lChar == rChar:
                return 0
            subs = 0
            while l >= 0 and r < len(s) and s[l] == lChar and s[r] == rChar:
                l -= 1
                r += 1
                subs += 1
            return subs
        ans = 0
        for i in range(len(s)-1):
            ans += countSubs(i, i+1)
        return ans
            
            
        