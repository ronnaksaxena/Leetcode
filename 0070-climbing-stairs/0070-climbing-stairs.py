class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        1 2 3 5 8 13 20 28
        1 2 3 4 5 6 7 8
        
        fib = 3
        
        '''
        if n == 1 or n == 2:
            return n
        
        first, second = 1, 2
        for _ in range(3, n+1):
            first, second = second, first + second
            
        return second
        