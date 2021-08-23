class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        w1, w2 = len(word1), len(word2)
        
        DP = [[0 for _ in range(w2+1)] for _ in range(w1+1)]
        
        for row in range(len(DP)):
            DP[row][0] = row
            
        for col in range(len(DP[0])):
            DP[0][col] = col
            
        
        #         keep, insert, delete, replace
        #                     i
        #           replace   insert
        #         j delete    sub
        #
        #
        
        
        for i in range(1, len(DP)): # word1
            for j in range(1, len(DP[0])):  #word2
                if word1[i-1] == word2[j-1]:
                    DP[i][j] = DP[i-1][j-1]
                else:
                    DP[i][j] = 1 + min(DP[i-1][j], DP[i-1][j-1], DP[i][j-1])
                    
        return DP[-1][-1]
                
