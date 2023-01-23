class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        text1 = "abcde"
        text2 = "ace" 
        
        '' a b c d e
     ''  0 0 0 0 0 0 
     a   0 1 1 1 1 1
     c   0 1 1 2 2 2 
     e   0 1 1 2 2 3
     
     if t1[j-1] == t2[i-1]:
        DP[i][j] = 1 + DP[i-1][j-1]
    else:
        DP[i][j] = max(DP[i-1][j], DP[i][j-1])
        
        '''
        
        DP = [[0 for _ in range(len(text1)+1)] for _ in range(len(text2)+1)]
        
        for i in range(1, len(DP)):
            for j in range(1, len(DP[0])):
                if text1[j-1] == text2[i-1]:
                    DP[i][j] = 1 + DP[i-1][j-1]
                else:
                    DP[i][j] = max(DP[i-1][j], DP[i][j-1])
                    
        return DP[-1][-1]
        