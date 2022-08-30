class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1 # Can't form a schedule
        memo = {}
        def dp(i, day):
            # Base case if on last day must return max of jobs remaining
            if day == d:
                return max(jobDifficulty[i:])
            # Iterate through all options while leaving (d-day) jobs left
            if (i, day) not in memo:
                hardest = float('-inf')
                best = float('inf')
                for j in range(i, n - (d-day)):
                    hardest = max(jobDifficulty[j], hardest)
                    best = min(best, hardest + dp(j+1, day+1))
                memo[(i, day)] = best
            return memo[(i, day)]
            
        
        return dp(0, 1)
