class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        t = s[::-1] #reversed s
        
        DP = [[0 for _ in range(n+1)] for _ in range(n+1)]
        
        for i in range(1,n+1): #chars in s
            for j in range(1,n+1): #chars in t
                
                if s[i-1]==t[j-1]:
                    DP[i][j] = 1 + DP[i-1][j-1]
                    
                else:
                    DP[i][j] = max(DP[i-1][j],DP[i][j-1])
                    
                    
                    
        return DP[-1][-1]
                
                
