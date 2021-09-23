class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        w, a = len(word), len(abbr)
        i, j = 0 , 0 #word, abbr
        
        while i < w and j < a:
            if word[i] == abbr[j]:
                i += 1
                j += 1
                continue
            
            if not abbr[j].isnumeric() or abbr[j] == '0':
                return False
            
            start = j
            
            while j < a and abbr[j].isnumeric():
                j += 1
            
            num = int(abbr[start:j])
            i += num
            
        return i == w and j == a
