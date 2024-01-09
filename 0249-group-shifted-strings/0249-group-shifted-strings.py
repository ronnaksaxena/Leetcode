class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        '''
        a b c
        
        b c d
         +1 +1
         
        Generate hash key by finding root string where s[0] starts with a
        
        Time: O(NxK) 
        Space: O(NxK) where n is strings in strings and K is max length of a string
        '''
        
        def shiftLetter(c, shiftAmt):
            shiftAmt = (ord(c) - shiftAmt - ord('a'))% 26
            return chr(shiftAmt + ord('a'))
        
        def getHash(word):
            # Find shift amount from first letter
            shiftAmt = ord(word[0]) - ord('a')
            res = ''.join(shiftLetter(c, shiftAmt) for c in word)
            return res
        
        group = collections.defaultdict(list) # {hash of letter: [list of words with that hash]}
        for s in strings:
            hashV = getHash(s)
            group[hashV].append(s)
        return group.values()