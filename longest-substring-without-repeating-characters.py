class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        chars = set()
        mlen = 0
        R = L = 0
        while R < len(s):
            if s[R] not in chars:
                chars.add(s[R])
                R += 1
                mlen = max(mlen,len(chars))
            else:
                chars.remove(s[L])
                L += 1
        return mlen
