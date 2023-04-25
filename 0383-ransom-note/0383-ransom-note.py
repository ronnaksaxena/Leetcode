class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = collections.Counter(magazine)
        
        for c in ransomNote:
            if not mag[c]:
                return False
            else:
                mag[c] -= 1
        return True
        