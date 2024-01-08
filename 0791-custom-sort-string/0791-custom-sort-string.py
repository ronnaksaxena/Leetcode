class Solution:
    def customSortString(self, order: str, s: str) -> str:
        '''
        input order(string), s(string)
        outpt: string
        
        - garunteed every char in s in order
        - lowercase english letter
        - not null
        
        Idea: build reordered s
        - map of frequencies of s
        - reOrderedS = []
        - loop through chars in order
            - if char in map:
                - append char * freq to reOrderedS list
        - return joined list
        
        N is length of s
        M is length of order
        Time: O(N + M) n to biuld map from s and M to iterate through order
        Space: O(N) for m
        '''
        
        freq = collections.Counter(s)
        reOrderedS = []
        
        for c in order:
            if c in freq:
                reOrderedS.append(c * freq[c])
                
        remainingChars = set(s).difference(set(order))
        for c in remainingChars:
            reOrderedS.append(c * freq[c])
        
        return ''.join(reOrderedS)
        