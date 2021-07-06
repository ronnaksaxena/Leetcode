class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-','').upper()
        ans = []
        chars = 0
        for i in range(len(s)-1,-1,-1):
            if i < k and chars%k==0:
                ans.insert(0, s[:i+1])
                break
            ans.insert(0, s[i])
            chars += 1
            if chars%k==0:
                ans.insert(0,'-')
        return ''.join(ans)
