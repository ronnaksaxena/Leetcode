class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def countVowels(word):
            return sum(c in 'aAeEiIoOuU' for c in word)
        
        return countVowels(s[:len(s)//2]) == countVowels(s[len(s)//2:])
        