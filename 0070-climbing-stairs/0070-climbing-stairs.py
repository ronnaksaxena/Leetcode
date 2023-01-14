class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        first, second = 1, 2
        
        for _ in range(3, n+1):
            second, first = first + second, second
            
        return second
            
        