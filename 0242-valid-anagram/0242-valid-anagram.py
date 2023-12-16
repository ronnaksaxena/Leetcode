class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted([c for c in s]) == sorted([c for c in t])
        