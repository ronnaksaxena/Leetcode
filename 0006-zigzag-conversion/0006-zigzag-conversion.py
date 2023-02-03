class Solution:
    def convert(self, s: str, numRows: int) -> str:
        '''
        [
        [P, I, N]
        [A, L, S, I, G]
        [Y, A, H, R]
        [P, I]
        ]
        
        arr[row] -> [chars in row ordered by col]
        
        Time: O(n) where n is lenght of string
        Space: O(n) for 2D array
        
        Edge Case:
        • curR and remaining chars is < numRow, want to stay inbounds of string
        
        '''
        curRow = 0
        stringIndex = 0
        zigzag = [[] for _ in range(numRows)]
        
        while stringIndex < len(s):
            if curRow == 0:
                for _ in range(numRows):
                    # Out of chars
                    if stringIndex >= len(s):
                        break
                    zigzag[curRow].append(s[stringIndex])
                    curRow += 1
                    stringIndex += 1
                curRow = (curRow-2) if numRows > 1 else 0 # Edge Case if 1 row
            else:
                zigzag[curRow].append(s[stringIndex])
                curRow = (curRow-1) if numRows > 1 else 0
                stringIndex += 1
                
        output = []
        for row in zigzag:
            output.append(''.join(row))
        return ''.join(output)
            
            
            
            
        
        