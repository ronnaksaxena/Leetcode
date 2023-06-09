class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters)
        
        while l < r:
            m = l + (r-l)//2
            if ord(letters[m]) <= ord(target):
                l = m + 1
            else:
                r = m
        return letters[l] if l < len(letters) else letters[0]
        