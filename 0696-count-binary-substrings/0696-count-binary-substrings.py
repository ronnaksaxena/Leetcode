class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = [1]
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                groups.append(1)
            else:
                groups[-1] += 1
        substrings = 0
        for i in range(1, len(groups)):
            substrings += min(groups[i-1], groups[i])
        return substrings
            
            
            
        