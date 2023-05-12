class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        @cache
        def dp(i):
            # terminal condition
            if i >= len(questions):
                return 0
            # decide to pick or skip
            else:
                points, skip = questions[i]
                return max(dp(i+1), points + dp(i+1+skip))
        
        return dp(0)
        