class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        keys = {c:i for i, c in enumerate(order)}
        
        for first, second in zip(words, words[1:]):
            foundDif = False
            for a, b in zip(first, second):
                if a != b:
                    if keys[a] > keys[b]:
                        return False
                    foundDif = True
                    break
            if not foundDif and len(first) > len(second):
                return False
            
        return True
        