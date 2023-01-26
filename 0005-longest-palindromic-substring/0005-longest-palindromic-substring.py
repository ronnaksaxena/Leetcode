class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        # Start and end indices of longest Palindrom found
        start, end = 0, 0
        n = len(s)
        
        DP = [[False for _ in range(n)] for _ in range(n)]
        # All single char substrings are palindromes
        for i in range(n):
            DP[i][i] = True
        # Check if any 2 length substrings are palindromes
        for i in range(n-1):
            if s[i] == s[i+1]:
                DP[i][i+1] = True
                if not start and not end:
                    start, end = i, i+1
        # Compare for all lengths k
        for k in range(2,n):
            for i in range(n):
                j = k+i
                # String too long
                if j == n:
                    break
                # DP[i+1][j-1] is subproblem, i+1 is next start, j-1 is prev end
                if DP[i+1][j-1] and s[i]==s[j]:
                    DP[i][j] = True
                    if j-i > end-start:
                        start, end = i, j
        # +1 since end if exlcusive           
        return s[start:end+1]
                        
                        
                        
                    
                    
                    
                
                
                
                
                
                
                
            
            
            
            
            
            