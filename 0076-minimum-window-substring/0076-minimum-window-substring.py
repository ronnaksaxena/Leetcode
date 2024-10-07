import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        Qs:
        - input s: String, t: String
        - output: String
        output- each char in t 1 ... * in ouptut
        - if not solution return empty string
        - Case senstive
        - only letters in both inputs
        - no whitespace
        - No memory constraints

        EDGE CASES:
        - if s or t is empty string: output empty string
        - char in t occurs multiple times in window in s
        - if multiple valid substrings of same lenght return either

        BRUTE FORCE: iterate thorughrt all substrings and check if they contain at leaast 1 char in t O(n^3)

        IDEA: Sliding Window

        s = "ADOBEBCODEBANC", t = "AAABC"
                        l
                          r
        Output: "BANC"

        CharsInWindow {char: frequency} A: 3, D: 1... B: 1, C: 0

        COME BACK: terminate after last char or include?

        IMPLEMENTATION
        if s or t empty: return ''
        CharsInWindow {char: frequency} 
        l = 0
        r = 0
        contains = 0 += 1
        requires = len(t)

        while contains == requires:
            check for a shorter valid substring
            increment l until no longer valid

        ALGO:
        count chars and frequencies tMap => {chars: frequencies}
        init vars
        init minSubstring = ''
        l = 0
        loop r for lenght of string
            - update CharsInWindow [s[r]] += 1
            - if CharsInWindow[s[r]]  == tMap[s[r]]:
                contains += 1
            - while contains == requires:
                if (r-l+1) < minSubstring:
                    minSubStirng = s[l:r+1]
                charsInMap[s[l]] -= 1
                if charsInMap[s[l]] < tMap[s[l]]:
                    contain -= 1
                l += 1
        return minSubstring


        Time: O(tLength + sLength) to init tMap and iterate throguht s
        Space: O(tLength + sLength) to store maps for both
        '''

        if not t or not s:
            return ''
        tMap = collections.Counter(t) # {charinT: frequency}
        charsInWindow = collections.defaultdict(int)
        l = 0
        minSubstring = ''
        requires = len(tMap)
        contains = 0

        for r in range(len(s)):
            charsInWindow[s[r]] += 1
            if charsInWindow[s[r]] == tMap[s[r]]:
                contains += 1
            # print(f'{s[l:r+1]}, contains {contains}, requries {requires}')
            # Found valid substring
            while contains == requires:
                if minSubstring == '' or (r-l+1) < len(minSubstring):
                    minSubstring = s[l:r+1]
                charsInWindow[s[l]] -= 1
                if charsInWindow[s[l]] < tMap[s[l]]:
                    contains -= 1
                l += 1

        return minSubstring

        '''
        s = "ADOBECODEBANC", t = "ABC"
             l
                  r 

        map = {A:1, D:1, O:1, B: 1, E: 1, C: 1}
        contains = 3
        requires = 3

        '''


        
        