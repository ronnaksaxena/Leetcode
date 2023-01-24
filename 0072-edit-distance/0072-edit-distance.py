class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        1. Do nothing
        2. Insert Letter
        3. Delete Letter
        4. Replace Letter
        
        word1 = "horse", word2 = "ros"
        '' h o r s e
    ''  0  1 2 3 4 5
    r   1  1 2 2 3 4
    o   2
    s   3
    
    if word1[j] != word2[i]:
        DP[i][j] = 1 + min(DP[i-1][j-1], DP[i-1][j], DP[i][j-1])
    else:
        DP[i][j] = min(DP[i-1][j-1], DP[i-1][j], DP[i][j-1])
        '''
        
        DP = [[0 for _ in range(len(word1)+1)] for _ in range(len(word2)+1)]
        # Set base cases
        for c in range(len(DP[0])):
            DP[0][c] = c
        for r in range(len(DP)):
            DP[r][0] = r
        # Bottom Up
        for i in range(1, len(DP)):
            for j in range(1, len(DP[0])):
                if word1[j-1] != word2[i-1]:
                    DP[i][j] = 1 + min(DP[i-1][j-1], DP[i][j-1], DP[i-1][j])
                else:
                    DP[i][j] = DP[i-1][j-1]
        return DP[-1][-1]
        
        
        
        
        
        