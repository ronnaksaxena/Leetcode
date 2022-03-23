class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        '''
        aeiouuc
         l
              r
        
        TV = 4
        map = {a: 0, e: 0, i: 0, o: 0, u: 0}
        
        
        '''
        
        maps = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
        # k and i are two pointers in typical same direction sliding window problem, j is used to mark start point
        j, k, vow, res = 0, 0, 0, 0
        for i in range(len(word)):
            if word[i] in maps:
                maps[word[i]] += 1
                if maps[word[i]] == 1:
                    vow += 1
                while vow == 5:
                    maps[word[k]] -= 1
                    if maps[word[k]] == 0:
                        vow -= 1
                    k += 1
                res += k-j
            else:
                # reset pointers and maps
