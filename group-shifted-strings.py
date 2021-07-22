class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        
        def canShift(word1, word2):
            if word1==word2:
                return True
            alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
            w1, w2 = list(word1), list(word2)
            
            for i in range(26):
                for i in range(len(w2)):
                    w2[i] = alpha[(alpha.index(w2[i]) + 1)%26]
                
                if w2 == w1:
                    return True
            
            return False
            
            
        
        output = []
        
        map = collections.defaultdict()
        
        for word in strings:
            if len(word) not in map:
                map[len(word)] = {word : [word]}
            else:
                foundShift = False
                for shiftCand in map[len(word)]:
                    if canShift(shiftCand, word):
                        map[len(word)][shiftCand].append(word)
                        foundShift = True
                        break
                if not foundShift:
                    map[len(word)][word] = [word]
        
​
        for lens in map.keys():
