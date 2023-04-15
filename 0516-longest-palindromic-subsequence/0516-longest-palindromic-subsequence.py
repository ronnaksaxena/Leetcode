class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        '''
        if s[i-1] == s[j-1]:
            DP[i][j] = DP[i-1][j-1] + 1
        else:
            DP[i][j] = max(DP[i-1][j], DP[i][j-1])
         '' b b b a b
     ''  0  0 0 0 0 0
     b   0  1 1 1 1 1
     b   0
     b   0
     a   0
     b   0
        '''
        n = len(s)
        revS = s[::-1]
        # +1 for empty stirng base case
        DP = [[0 for _ in range(n+1)] for _ in range(n+1)]
        
        for i in range(1, len(DP)):
            for j in range(1, len(DP[0])):
                if s[i-1] == revS[j-1]:
                    DP[i][j] = DP[i-1][j-1] + 1
                else:
                    DP[i][j] = max(DP[i-1][j], DP[i][j-1])
        return DP[-1][-1]
        