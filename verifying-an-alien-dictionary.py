class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        map = {}
        for i in range(len(order)):
            map[order[i]] = i
            
        
        for first,second in zip(words,words[1:]):
            
            foundDif = False
            
            for a,b in zip(first,second):
                if a != b:
                    if map[a] > map[b]:
                        return False
                    else:
                        foundDif = True
                        break
            if not foundDif and len(first) > len(second):
                return False
            
        return True
