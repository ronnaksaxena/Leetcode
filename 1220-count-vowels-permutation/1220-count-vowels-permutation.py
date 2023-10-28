class Solution:
    def countVowelPermutation(self, n: int) -> int:
        def nextVowel(c):
            # returns a list of next possible vowels
            if c == '':
                return ['a','e','i','o','u']
            if c == 'a':
                return ['e']
            elif c == 'e':
                return ['a', 'i']
            elif c == 'i':
                return ['a', 'e', 'o', 'u']
            elif c == 'o':
                return ['i', 'u']
            else:
                # u
                return ['a']
        output = set()
        curPerm = []
        @cache
        def backtrack(lastChar, length):
            # find all possible permutations
            if length == n:
                return 1
            possibleVowels = nextVowel(lastChar)
            ans = 0
            for v in possibleVowels:
                ans += backtrack(v, length+1)
            return ans
        
        return backtrack('', 0)%(10**9 +7)
        