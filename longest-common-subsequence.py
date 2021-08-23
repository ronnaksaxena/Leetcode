class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        n, m = len(text1), len(text2)
        
        DP = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        for i in range(1,m+1): #text2 chars
            for j in range(1,n+1): #text1 chars
                
                if text2[i-1] == text1[j-1]:
                    DP[i][j] = 1 + DP[i-1][j-1]
                else:
                    DP[i][j] = max(DP[i-1][j], DP[i][j-1])
                    
                    
        return DP[-1][-1]
