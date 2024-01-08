class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        '''
        input = string '(' / ')'
        output = int => number of changes
        
        "())"
           
        []
        "((("
        [(,(,(] 
        
        numOfMoves += 1 for every missing match
        at end of loop
        numOfMoves += length of stack
        
        Time: O(n)
        Space: O(n)
        
        Optimizations:
        - openP = 0
        - loop throught s:
            if char is ):
                check there is open to map to closing
                if openP > 0:
                    openP -= 1
                else:
                    numOfMoves += 1
            if char is (:
                openP += 1
        - numOfMoves += openP
        Time: O(n)
        Space: O(1)
        '''
        
        openP = 0
        numOfMoves = 0
        for c in s:
            if c == ')':
                if openP > 0:
                    openP -= 1
                else:
                    numOfMoves += 1
            else:
                # Open parenthesis
                openP += 1
        return numOfMoves + openP
        